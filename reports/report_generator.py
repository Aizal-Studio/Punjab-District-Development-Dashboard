from reportlab.lib import colors
from reportlab.platypus import Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

# from reportlab.graphics.shapes import Drawing
# from reportlab.graphics.charts.barcharts import VerticalBarChart
# from reportlab.graphics.charts.textlabels import Label

import datetime
import os


# ==========================================
# Color Theme
# ==========================================

PRIMARY = colors.HexColor("#145A32")
SECONDARY = colors.HexColor("#1E8449")
LIGHT = colors.HexColor("#EAF7EA")
DARK = colors.HexColor("#154360")
GOLD = colors.HexColor("#B7950B")


styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.fontName = "Helvetica-Bold"
title_style.fontSize = 24
title_style.alignment = TA_CENTER
title_style.textColor = PRIMARY

heading_style = styles["Heading2"]
heading_style.fontName = "Helvetica-Bold"
heading_style.textColor = PRIMARY

normal_style = styles["BodyText"]
normal_style.fontSize = 11
normal_style.leading = 18


# ==========================================
# Helper Function
# ==========================================

def create_table(data):

    table = Table(
        data,
        colWidths=[2.8 * inch, 3.6 * inch]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), PRIMARY),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BACKGROUND",(0,1),(-1,-1),LIGHT),

        ("BOTTOMPADDING",(0,0),(-1,0),8),

        ("TOPPADDING",(0,0),(-1,-1),6),

        ("BOTTOMPADDING",(0,1),(-1,-1),6)

    ]))

    return table


# ==========================================
# Development Chart
# ==========================================

def development_chart(selected):
    return None
# ==========================================
# PDF REPORT
# ==========================================

def create_report(selected):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{selected['District']}_Development_Report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    story = []

    # ======================================
    # COVER PAGE
    # ======================================

    story.append(Spacer(1, 1.0 * inch))

    story.append(Paragraph(
        "Punjab District Development Dashboard",
        title_style
    ))

    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph(
        "<b>Evidence Based Development Planning Report</b>",
        heading_style
    ))

    story.append(Spacer(1, 0.45 * inch))

    story.append(Paragraph(
        f"<font size=18><b>{selected['District']} District</b></font>",
        styles["Title"]
    ))

    story.append(Spacer(1, 0.6 * inch))

    story.append(Paragraph(
        f"""
<b>Development Score:</b> {selected['DevelopmentScore']}<br/><br/>
<b>Population:</b> {int(selected['Population']):,}<br/><br/>
<b>Literacy Rate:</b> {selected['LiteracyRate']:.2f}%<br/><br/>
<b>Hospitals:</b> {selected['Hospitals']}<br/><br/>
<b>Total Schools:</b> {selected['TotalSchools']}
""",
        normal_style
    ))

    story.append(Spacer(1, 1.2 * inch))

    story.append(Paragraph(
        f"Generated on : {datetime.datetime.now().strftime('%d %B %Y')}",
        normal_style
    ))

    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph(
        "<b>Developed by AIZAL STUDIO</b>",
        heading_style
    ))

    story.append(PageBreak())

    # ======================================
    # EXECUTIVE SUMMARY
    # ======================================

    story.append(Paragraph(
        "Executive Summary",
        heading_style
    ))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph(
        """
This report provides a district level assessment using demographic,
education, healthcare and infrastructure indicators. The objective
is to support evidence based planning and identify sectors that
require further investment.
""",
        normal_style
    ))

    story.append(Spacer(1, 0.25 * inch))

    table_data = [

        ["Indicator", "Value"],

        ["District", selected["District"]],

        ["Population", f"{int(selected['Population']):,}"],

        ["Area (km²)", selected["Area"]],

        ["Population Density", f"{selected['Density']:.2f}"],

        ["Literacy Rate", f"{selected['LiteracyRate']:.2f}%"],

        ["Hospitals", selected["Hospitals"]],

        ["Hospital Beds", selected["Beds"]],

        ["Primary Schools", selected["PrimarySchools"]],

        ["Middle Schools", selected["MiddleSchools"]],

        ["High Schools", selected["HighSchools"]],

        ["Total Schools", selected["TotalSchools"]],

        ["Development Score", selected["DevelopmentScore"]],

        ["Punjab Rank", selected["Rank"]]

    ]

    story.append(create_table(table_data))

    story.append(Spacer(1, 0.35 * inch))

    story.append(Paragraph(
        "Overall Development Assessment",
        heading_style
    ))

    story.append(Spacer(1, 0.15 * inch))

    if float(selected["DevelopmentScore"]) >= 70:

        level = "Excellent"

    elif float(selected["DevelopmentScore"]) >= 50:

        level = "Good"

    elif float(selected["DevelopmentScore"]) >= 35:

        level = "Average"

    else:

        level = "Needs Improvement"

    story.append(Paragraph(
        f"""
Based on the available indicators, the overall development
status of <b>{selected['District']}</b> is classified as
<b>{level}</b>.
""",
        normal_style
    ))

    story.append(PageBreak())
        # ======================================
    # PAGE 3
    # Development Charts
    # ======================================

    story.append(Paragraph(
        "Development Indicators",
        heading_style
    ))

    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph(
    "Development chart is temporarily unavailable.",
    normal_style
))

    story.append(Paragraph(
    "Development chart is not available in the online version.",
    normal_style
))

    story.append(Spacer(1, 0.35 * inch))

    story.append(Paragraph(
        """
The chart above summarizes the district's performance across
major development sectors including education, health,
infrastructure and the overall development score.
""",
        normal_style
    ))

    story.append(PageBreak())

    # ======================================
    # PAGE 4
    # AI Recommendations
    # ======================================

    story.append(Paragraph(
        "AI Development Recommendations",
        heading_style
    ))

    story.append(Spacer(1, 0.25 * inch))

    recommendations = []

    if float(selected["LiteracyRate"]) < 60:
        recommendations.append(
            "Increase literacy programs and improve school enrollment."
        )

    if int(selected["Hospitals"]) < 10:
        recommendations.append(
            "Construct additional hospitals and strengthen healthcare services."
        )

    if int(selected["Beds"]) < 1000:
        recommendations.append(
            "Increase hospital bed capacity to improve healthcare access."
        )

    if int(selected["PrimarySchools"]) < 800:
        recommendations.append(
            "Expand primary education facilities in underserved areas."
        )

    if float(selected["DevelopmentScore"]) < 35:
        recommendations.append(
            "Prioritize this district in future provincial development planning."
        )

    if len(recommendations) == 0:

        story.append(Paragraph(
            """
This district performs well across the available indicators.
Continued investment and monitoring are recommended to maintain
its development progress.
""",
            normal_style
        ))

    else:

        for i, rec in enumerate(recommendations, start=1):

            story.append(Paragraph(
                f"{i}. {rec}",
                normal_style
            ))

            story.append(Spacer(1, 0.12 * inch))

    story.append(Spacer(1, 0.35 * inch))

    story.append(Paragraph(
        "Conclusion",
        heading_style
    ))

    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph(
        f"""
The analysis indicates that <b>{selected['District']}</b>
has a Development Score of
<b>{selected['DevelopmentScore']}</b>.
This report can assist planners, researchers and policy makers
in identifying priority sectors for future investment and
sustainable development.
""",
        normal_style
    ))

    story.append(Spacer(1, 0.35 * inch))

    story.append(Paragraph(
        "Technology Stack",
        heading_style
    ))

    tech = [
        ["Python"],
        ["Streamlit"],
        ["Pandas"],
        ["Plotly"],
        ["ReportLab"]
    ]

    tech_table = Table(tech, colWidths=[4 * inch])

    tech_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("BACKGROUND", (0,0), (-1,-1), LIGHT),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))

    story.append(tech_table)

    story.append(Spacer(1, 0.45 * inch))

    story.append(Paragraph(
        "<b>Developed By</b>",
        heading_style
    ))

    story.append(Paragraph(
        """<b>AIZAL STUDIO</b><br/>Data Analytics &amp; Visualization""",
        normal_style
    ))

    story.append(Paragraph(
        "Punjab District Development Dashboard",
        normal_style
    ))

    story.append(Paragraph(
        f"Report Generated: {datetime.datetime.now().strftime('%d %B %Y %I:%M %p')}",
        normal_style
    ))

    story.append(Spacer(1, 0.35 * inch))

    story.append(Paragraph(
        "<font size=9>This report has been generated automatically using the Punjab District Development Dashboard. The information is intended for educational and analytical purposes.</font>",
        normal_style
    ))

    # ======================================
    # BUILD PDF
    # ======================================

    doc.build(story)

    return filename