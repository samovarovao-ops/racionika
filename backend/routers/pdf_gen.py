from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from backend.storage import get_menu_data
from backend.calculator import calculate
from backend.models.schemas import PersonGroup
from fpdf import FPDF
import os

router = APIRouter()

FONT_REGULAR = "C:/Windows/Fonts/arial.ttf"
FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"


class PDF(FPDF):
    def header(self):
        self.set_font("arial", "B", 16)
        self.set_text_color(13, 148, 136)
        self.cell(0, 12, "\u0420\u0430\u0446\u0438\u043e\u043d\u0438\u043a\u0430", new_x="LMARGIN", new_y="NEXT")
        self.set_font("arial", "", 8)
        self.set_text_color(107, 114, 128)
        self.cell(0, 5, "\u0418\u043d\u0442\u0435\u043b\u043b\u0435\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0439 \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 \u0440\u0430\u0446\u0438\u043e\u043d\u043e\u0432", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(13, 148, 136)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("arial", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"\u0421\u0442\u0440. {self.page_no()}", align="C")

    def title_text(self, text):
        self.set_font("arial", "B", 13)
        self.set_text_color(13, 148, 136)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def subtitle_text(self, text):
        self.set_font("arial", "B", 11)
        self.set_text_color(16, 185, 129)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def info_line(self, label, value):
        self.set_font("arial", "B", 10)
        self.set_text_color(44, 62, 80)
        self.cell(55, 7, label)
        self.set_font("arial", "", 10)
        self.cell(0, 7, str(value), new_x="LMARGIN", new_y="NEXT")

    def price_line(self, label, value, bold=False, color=(44, 62, 80)):
        self.set_text_color(*color)
        style = "B" if bold else ""
        self.set_font("arial", style, 10)
        self.cell(70, 7, label)
        self.set_font("arial", "B" if bold else "", 11)
        self.cell(0, 7, f"{value} \u20bd", new_x="LMARGIN", new_y="NEXT")

    def table_header(self, cols):
        self.set_font("arial", "B", 8)
        self.set_fill_color(13, 148, 136)
        self.set_text_color(255, 255, 255)
        for w, txt in cols:
            self.cell(w, 7, txt, border=1, fill=True)
        self.ln()

    def table_row(self, cols, fill=False):
        self.set_font("arial", "", 8)
        self.set_text_color(44, 62, 80)
        if fill:
            self.set_fill_color(240, 248, 255)
        for w, txt in cols:
            self.cell(w, 6, str(txt), border=1, fill=fill)
        self.ln()


def _add_day(pdf, day, currency):
    d = day.model_dump() if hasattr(day, "model_dump") else day
    for meal in d["\u043f\u0440\u0438\u0451\u043c\u044b"]:
        pdf.subtitle_text(meal["\u041f\u0440\u0438\u0451\u043c"])
        pdf.table_header([(80, "\u0411\u043b\u044e\u0434\u043e"), (20, "\u0426\u0435\u043d\u0430"), (15, "\u041f\u043e\u0440\u0446."), (25, "\u0421\u0442\u043e\u0438\u043c.")])
        for i, b in enumerate(meal["\u0431\u043b\u044e\u0434\u0430"]):
            name = b["\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435_\u0431\u043b\u044e\u0434\u0430"]
            if len(name) > 45:
                name = name[:42] + "..."
            pdf.table_row([
                (80, name),
                (20, str(b["\u0426\u0435\u043d\u0430_\u0437\u0430_\u043f\u043e\u0440\u0446\u0438\u044e"])),
                (15, str(b["\u041f\u043e\u0440\u0446\u0438\u0438_\u043d\u0430_\u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430"])),
                (25, str(b["\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c_\u0441\u0442\u0440\u043e\u043a\u0438"])),
            ], fill=(i % 2 == 0))
        pdf.ln(2)
    pdf.set_font("arial", "B", 9)
    pdf.set_text_color(13, 148, 136)
    pdf.cell(0, 7, f"\u0418\u0442\u043e\u0433\u043e \u0437\u0430 \u0434\u0435\u043d\u044c: {d['\u0434\u043d\u0435\u0432\u043d\u0430\u044f_\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c']} {currency}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)


@router.post("/generate-pdf")
def generate_pdf(body: dict):
    menu_id = body.get("menu_id", "")
    groups_data = body.get("groups", [])
    days = body.get("days", 7)
    start_day = body.get("start_day", 1)

    menu_data = get_menu_data(menu_id)
    if menu_data is None:
        raise HTTPException(status_code=404, detail="\u041c\u0435\u043d\u044e \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e")

    try:
        groups = [PersonGroup(**g) for g in groups_data]
        result = calculate(menu_data, groups, days, start_day)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    from datetime import datetime
    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_font("arial", "", FONT_REGULAR)
    pdf.add_font("arial", "B", FONT_BOLD)
    pdf.add_page()

    pdf.set_font("arial", "", 9)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 7, f"\u0414\u0430\u0442\u0430: {now}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    DAYS = ["", "\u041f\u043d", "\u0412\u0442", "\u0421\u0440", "\u0427\u0442", "\u041f\u0442", "\u0421\u0431", "\u0412\u0441"]
    PROGS = {"Classic": "\u041a\u043b\u0430\u0441\u0441\u0438\u043a\u0430", "Balance": "\u0411\u0430\u043b\u0430\u043d\u0441", "Vegan": "\u0412\u0435\u0433\u0430\u043d"}
    TYPES = {0: "\u0432\u0437\u0440\u043e\u0441\u043b\u044b\u0439", 1: "\u0440\u0435\u0431\u0451\u043d\u043e\u043a"}

    pdf.title_text("\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b")
    for i, g in enumerate(result.groups):
        t = TYPES.get(g.children > 0, "")
        pdf.info_line(f"\u0427\u0435\u043b\u043e\u0432\u0435\u043a {i+1} ({t}):", PROGS.get(g.program, g.program))
    pdf.info_line("\u0414\u043d\u0435\u0439:", str(days))
    pdf.info_line("\u0421\u0442\u0430\u0440\u0442:", DAYS[start_day])
    pdf.ln(3)

    pdf.title_text("\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c")
    pdf.price_line("\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0432 \u0434\u0435\u043d\u044c:", result.per_day_cost)
    pdf.price_line("\u0418\u0442\u043e\u0433\u043e:", result.total_kit_price)
    if result.discount_percent > 0:
        pdf.price_line(f"\u0421\u043a\u0438\u0434\u043a\u043a\u0430 -{result.discount_percent}%:", f"-{result.discount_amount}")
        pdf.price_line("\u0421 \u0441\u043a\u0438\u0434\u043a\u043e\u0439:", result.final_price, bold=True, color=(39, 174, 96))
    pdf.price_line("\u0417\u0430 \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430 \u0432 \u0434\u0435\u043d\u044c:", result.per_person_per_day)
    pdf.ln(5)

    for gi, g in enumerate(result.groups):
        t = TYPES.get(g.children > 0, "")
        prog = PROGS.get(g.program, g.program)
        pdf.title_text(f"\u041f\u043b\u0430\u043d: \u0427\u0435\u043b\u043e\u0432\u0435\u043a {gi+1} ({t}) \u2014 {prog}")
        for day in g.plan:
            if pdf.get_y() > 220:
                pdf.add_page()
            day_num = day.День if hasattr(day, "День") else (day.get("День") if isinstance(day, dict) else "")
            pdf.subtitle_text(f"\u0414\u0435\u043d\u044c {day_num}")
            _add_day(pdf, day, result.currency)

    pdf_bytes = pdf.output()
    return Response(
        content=bytes(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=ration_report.pdf"},
    )
