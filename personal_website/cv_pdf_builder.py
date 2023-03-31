from fpdf import FPDF
from cv_pdf.resume import ed_experiences, w_experiences, certifications
from cv_pdf.sidebar import *
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings")

import django
django.setup()
from website.models import Experience

w_experiences = [e for e in Experience.objects.all() if e.exp_type == "W"]
print(w_experiences)


class PDF(FPDF):
    pdf_w = 210
    pdf_h = 297
    exp_entry_title_w = 100

    def header(self):
        # sidebar
        self.set_fill_color(223, 224, 224)
        self.rect(0, 0, 65, self.pdf_h, style="F")


pdf = PDF(orientation='P', unit='mm', format='A4')
# pdf.add_font(family="nunito-light", fname='cv_pdf\\Nunito-Light.ttf', uni=True)
# pdf.add_font(family="montserrat", fname='cv_pdf\\Montserrat-Medium.ttf', uni=True)

sidebar_v_spacing = 6
default_cell_height = 4.5


def print_main_separator(height):
    pdf.set_fill_color(223, 224, 224)
    pdf.rect(75, height, pdf.exp_entry_title_w, 1, "F")


def print_name():
    pdf.set_xy(75, 55)
    pdf.set_font("arial", "", 28)
    pdf.set_text_color(0, 109, 119)
    pdf.multi_cell(90, 12, "SIMONE MARTIN MAROTTA")
    print_main_separator(80)


def build_bio():
    pdf.image("cv_pdf\\foto.png", 10, 30, 40)
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(44, 50, 54)
    pdf.set_xy(10, 75)
    pdf.multi_cell(50, 5, short_bio, align="center")


def build_hobbies():
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("arial", "", 9)
    pdf.set_text_color(0, 109, 119)
    pdf.cell(50, 5, "HOBBIES", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(44, 50, 54)
    for h in hobbies:
        pdf.cell(50, 5, h, ln=True)


def build_skills():
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("arial", "", 9)
    pdf.set_text_color(0, 109, 119)
    pdf.cell(50, 5, "SKILLS", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(44, 50, 54)
    for l in lang_skills:
        pdf.cell(20, 5, l[0], ln=False)
        pdf.cell(20, 5, "", ln=True)
        pdf.set_fill_color(0, 109, 119)
        pdf.rect(38, pdf.get_y() - 3, (20 * l[1]) / 100, 1, "F")
    for c in comp_skills:
        pdf.cell(20, 5, c[0], ln=False)
        pdf.cell(20, 5, "", ln=True)
        pdf.set_fill_color(0, 109, 119)
        pdf.rect(38, pdf.get_y() - 3, (20 * c[1]) / 100, 1, "F")


def build_contacts():
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("arial", "", 9)
    pdf.set_text_color(0, 109, 119)
    pdf.cell(50, 5, "CONTACTS", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(44, 50, 54)
    pdf.cell(50, 5, f"PHONE {contacts['phone']}", ln=True)
    pdf.cell(50, 5, f"MAIL {contacts['mail']}", ln=True)
    pdf.cell(50, 5, f"WEB {contacts['web']}", ln=True)


def build_references():
    pdf.set_xy(10, 10)
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("arial", "", 9)
    pdf.set_text_color(0, 109, 119)
    pdf.cell(50, 5, "REFERENCES", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(44, 50, 54)
    for r in references:
        pdf.cell(50, 5, r["name"], ln=True)
        pdf.cell(50, 5, r["role"], ln=True)
        pdf.cell(50, 5, r["institution"], ln=True)
        pdf.cell(50, 5, r["location"], ln=True)
        pdf.cell(50, 5, r["phone"], ln=True)
        pdf.cell(50, 5, r["mail"], ln=True)
        pdf.cell(50, 3, "", ln=True)
        pdf.set_fill_color(0, 109, 119)
        pdf.rect(10, pdf.get_y(), 45, 0.2, "F")
        pdf.cell(50, 5, "", ln=True)


def build_exp_title(title):
    # section title
    pdf.set_x(75)
    pdf.set_font("arial", "", 13)
    pdf.set_text_color(0, 109, 119)
    pdf.cell(pdf.exp_entry_title_w, 5, title, ln=True)
    # set font for entries
    pdf.set_font("helvetica", "", 9)


def build_w_exp():
    pdf.set_y(85)
    build_exp_title("Work Experience")

    # entries
    pdf.set_text_color(44, 50, 54)
    for e in w_experiences:
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, default_cell_height, e.name, ln=True)
        pdf.set_x(75)
        institution = e.institution.all()[0]
        place = institution.place.all()[0].name
        date = str(e.start_time.year) + " - " + str(e.end_time.year) if e.start_time.year != e.end_time.year else str(e.start_time.year)
        pdf.cell(pdf.exp_entry_title_w, default_cell_height, date + " | " + institution.name + " | " + place,
                 ln=True, link=institution.url)
        for p in e.points.split("\n"):
            pdf.set_x(80)
            pdf.multi_cell(pdf.exp_entry_title_w, default_cell_height, "- " + p)
    global CURRENT_Y
    CURRENT_Y = pdf.get_y()


def build_e_exp():
    build_exp_title("Education")

    pdf.set_text_color(44, 50, 54)
    for e in ed_experiences:
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, default_cell_height, e["name"], ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, default_cell_height, e["date"], ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, default_cell_height, e["institution"] + e["location"], ln=True, link=e["url"])
        for p in e["points"]:
            pdf.set_x(80)
            pdf.multi_cell(pdf.exp_entry_title_w, default_cell_height, "- " + p)
    global CURRENT_Y
    CURRENT_Y = pdf.get_y()


def build_certifications():
    build_exp_title("Certifications")

    pdf.set_text_color(44, 50, 54)
    for c in certifications:
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
        pdf.set_x(75)
        pdf.set_font("helvetica")
        pdf.cell(5, 1, "- ")
        pdf.set_font("helvetica", style="U")
        pdf.cell(pdf.exp_entry_title_w, 1, c["title"], ln=True, link=c["url"])


def print_experiences():
    build_w_exp()
    build_references()
    pdf.set_y(CURRENT_Y)
    pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
    print_main_separator(pdf.get_y())
    pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
    build_e_exp()
    pdf.set_y(CURRENT_Y)
    pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
    print_main_separator(pdf.get_y())
    pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
    build_certifications()


def print_sidebar():
    build_bio()
    build_hobbies()
    build_skills()
    build_contacts()


def main():
    pdf.add_page()
    pdf.set_auto_page_break(True, margin=20)
    pdf.image("cv_pdf\\top.png", 0, 0, pdf.pdf_w)

    print_name()
    print_sidebar()
    print_experiences()

    pdf.image("cv_pdf\\bottom.png", 0, 242, pdf.pdf_w)

    pdf.output('CV Simone Martin Marotta.pdf')


if __name__ == "__main__":
    main()
