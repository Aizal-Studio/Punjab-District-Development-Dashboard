import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="Punjab District Development Dashboard",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from reports.report_generator import create_report


# ==============================
# Theme
# ==============================

st.markdown("""
<style>

.stApp{
    background:#F4F6F7;
}

section[data-testid="stSidebar"]{
    background:#145A32;
}

section[data-testid="stSidebar"] *{
    color:white;
}

div[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:12px;
    border-left:5px solid #145A32;
}

.stButton button{
    background:#145A32;
    color:white;
    border-radius:8px;
}

.stDownloadButton button{
    background:#145A32;
    color:white;
    border-radius:8px;
}

</style>
""", unsafe_allow_html=True)



# ==============================
# Header
# ==============================

st.markdown("""
<div style="
background:#145A32;
padding:25px;
border-radius:15px;
">

<h1 style="color:white;text-align:center;">
Government of Punjab
</h1>

<h3 style="color:white;text-align:center;">
Planning & Development Department
</h3>

<h2 style="color:#FFD700;text-align:center;">
Punjab District Development Dashboard
</h2>

<p style="color:white;text-align:center;">
Evidence Based Development Planning
</p>

<p style="color:white;text-align:center;">
Developed by AIZAL STUDIO
</p>

</div>
""", unsafe_allow_html=True)



# ==============================
# Load Data
# ==============================

df = pd.read_csv(
    "data/final/district_indicators.csv"
)


df = df.fillna(0)


for col in df.columns:

    if col != "District":
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )


df = df.fillna(0)



# ==============================
# Sidebar
# ==============================
logo = Image.open("assets/logo.png")

st.sidebar.image(
    logo,
    use_container_width=True
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <h2 style='text-align:center;color:#145A32;'>
    AIZAL STUDIO
    </h2>
    """,
    unsafe_allow_html=True
)

st.sidebar.caption("Punjab District Development Dashboard")


st.sidebar.title(
    "🏛 Dashboard Navigation"
)


st.sidebar.markdown("---")


st.sidebar.success(
    "System Status: Online"
)


st.sidebar.write(
    "Government of Punjab"
)

st.sidebar.write(
    "Districts: 36"
)

st.sidebar.write(
    "Census: 2023"
)

st.sidebar.write(
    "Health Data: 2024"
)

st.sidebar.write(
    "Education Data: 2022-23"
)


st.sidebar.markdown("---")


districts = sorted(df["District"].unique())

district = st.sidebar.selectbox(
    "📍 Select District",
    districts,
    index=0,
    key="district_select"
)


selected = df[
    df["District"] == district
].iloc[0]

st.sidebar.success(
    f"Selected: {district}"
)

st.sidebar.markdown("---")


districts = sorted(df["District"].unique())

district2 = st.sidebar.selectbox(
    "⚖ Compare District",
    districts,
    index=1,
    key="compare_select"
)


selected2 = df[
    df["District"] == district2
].iloc[0]


st.sidebar.markdown("---")


st.sidebar.info(
f"""
Selected District:

{selected['District']}

Rank:

{int(selected['Rank'])}/36

Development Score:

{float(selected['DevelopmentScore']):.2f}
"""
)


# ==============================
# Main KPI
# ==============================


col1,col2,col3,col4 = st.columns(4)


col1.metric(
    "Total Districts",
    len(df)
)


col2.metric(
    "Population",
    f"{int(df['Population'].sum()):,}"
)


col3.metric(
    "Average Literacy",
    f"{df['LiteracyRate'].mean():.2f}%"
)


col4.metric(
    "Average Score",
    f"{df['DevelopmentScore'].mean():.2f}"
)


st.divider()


st.header(
    f"📍 {selected['District']} Profile"
)
# ==============================
# Development Status
# ==============================

rank = int(selected["Rank"])
score = float(selected["DevelopmentScore"])


if rank <= 5:

    status = "🟢 Highly Developed"

elif rank <= 15:

    status = "🟡 Moderately Developed"

elif rank <= 25:

    status = "🟠 Developing"

else:

    status = "🔴 Needs Immediate Development"



st.info(
f"""
Development Status: {status}

Punjab Rank: {rank}/36

Development Score: {score:.2f}
"""
)



# ==============================
# District Indicators
# ==============================


c1,c2,c3 = st.columns(3)


c1.metric(
    "👥 Population",
    f"{int(selected['Population']):,}"
)


c2.metric(
    "📚 Literacy Rate",
    f"{float(selected['LiteracyRate']):.2f}%"
)


c3.metric(
    "⭐ Development Score",
    f"{float(selected['DevelopmentScore']):.2f}"
)



c4,c5,c6 = st.columns(3)


c4.metric(
    "🏥 Health Index",
    f"{float(selected['HealthIndex']):.2f}"
)


c5.metric(
    "🎓 Education Index",
    f"{float(selected['EducationIndex']):.2f}"
)


c6.metric(
    "🛣 Infrastructure Index",
    f"{float(selected['InfrastructureIndex']):.2f}"
)



st.divider()



# ==============================
# Profile Tables
# ==============================


left,right = st.columns(2)



with left:

    st.subheader(
        "Basic Information"
    )


    profile = pd.DataFrame({

        "Indicator":[

            "Population",
            "Literacy Rate",
            "Development Score",
            "Punjab Rank"

        ],

        "Value":[

            f"{int(selected['Population']):,}",
            f"{float(selected['LiteracyRate']):.2f}%",
            f"{score:.2f}",
            f"{rank}/36"

        ]

    })


    st.dataframe(
        profile,
        width="stretch",
        hide_index=True
    )



with right:

    st.subheader(
        "Education & Health"
    )


    profile2 = pd.DataFrame({

        "Indicator":[

            "Hospitals",
            "Beds",
            "Primary Schools",
            "Middle Schools",
            "High Schools",
            "Total Schools"

        ],

        "Value":[

            int(selected["Hospitals"]),
            int(selected["Beds"]),
            int(selected["PrimarySchools"]),
            int(selected["MiddleSchools"]),
            int(selected["HighSchools"]),
            int(selected["TotalSchools"])

        ]

    })


    st.dataframe(
        profile2,
        width="stretch",
        hide_index=True
    )



st.divider()



# ==============================
# Executive Summary
# ==============================


st.subheader(
    "📄 Executive Summary"
)


summary = f"""

{selected['District']} district is ranked
{rank} among the 36 districts of Punjab.

The district population is
{int(selected['Population']):,}.

Literacy rate is
{float(selected['LiteracyRate']):.2f}%.

Development score is
{score:.2f}.

This dashboard analyzes education,
health, infrastructure and demographic
indicators for evidence based planning.

"""


st.success(summary)



st.divider()



# ==============================
# Charts
# ==============================


st.header(
    "📊 Development Analytics"
)



top10 = (
    df.sort_values(
        "DevelopmentScore",
        ascending=False
    )
    .head(10)
)



fig1 = px.bar(

    top10,

    x="District",

    y="DevelopmentScore",

    color="DevelopmentScore",

    text="DevelopmentScore",

    title="Top 10 Developed Districts"

)


fig1.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_x=0.5
)


st.plotly_chart(
    fig1,
    width="stretch"
)



# Literacy Chart


fig2 = px.bar(

    df.sort_values(
        "LiteracyRate",
        ascending=False
    ),

    x="District",

    y="LiteracyRate",

    color="LiteracyRate",

    title="District Literacy Rate"

)


fig2.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_x=0.5
)


st.plotly_chart(
    fig2,
    width="stretch"
)



# Hospital Beds Chart


fig3 = px.bar(

    df.sort_values(
        "Beds",
        ascending=False
    ),

    x="District",

    y="Beds",

    color="Beds",

    title="Hospital Bed Capacity"

)


fig3.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_x=0.5
)


st.plotly_chart(
    fig3,
    width="stretch"
)


st.divider()
# ==============================
# Population Distribution
# ==============================

st.header(
    "👥 Population Distribution"
)


fig4 = px.pie(

    df.head(10),

    names="District",

    values="Population",

    hole=0.45,

    title="Population Share of Top 10 Districts"

)


fig4.update_layout(
    paper_bgcolor="white",
    title_x=0.5
)


st.plotly_chart(
    fig4,
    width="stretch"
)


# =====================================
# Punjab District Interactive Map
# =====================================

st.header("🗺 Punjab District Development Map")

fig_map = px.scatter_map(
    df,
    lat="Latitude",
    lon="Longitude",
    color="DevelopmentScore",
    size="Population",
    hover_name="District",
    hover_data={
        "DevelopmentScore": True,
        "Population": True,
        "LiteracyRate": True,
        "Latitude": False,
        "Longitude": False
    },
    zoom=6,
    center={
        "lat":31.2,
        "lon":72.8
    },
    color_continuous_scale="Viridis",
    height=650
)

fig_map.update_layout(
    map_style="open-street-map",
    margin=dict(l=0,r=0,t=40,b=0)
)

st.plotly_chart(
    fig_map,
    width="stretch"
)

st.divider()
st.divider()



# ==============================
# District Comparison
# ==============================


st.header(
    "⚖ District Comparison"
)



comparison = pd.DataFrame({

    "Indicator":[

        "Population",
        "Literacy Rate",
        "Hospitals",
        "Beds",
        "Total Schools",
        "Development Score"

    ],


    selected["District"]:[

        int(selected["Population"]),
        float(selected["LiteracyRate"]),
        int(selected["Hospitals"]),
        int(selected["Beds"]),
        int(selected["TotalSchools"]),
        float(selected["DevelopmentScore"])

    ],


    selected2["District"]:[

        int(selected2["Population"]),
        float(selected2["LiteracyRate"]),
        int(selected2["Hospitals"]),
        int(selected2["Beds"]),
        int(selected2["TotalSchools"]),
        float(selected2["DevelopmentScore"])

    ]

})



st.dataframe(

    comparison,

    width="stretch",

    hide_index=True

)



compare = pd.DataFrame({

    "District":[

        selected["District"],
        selected2["District"]

    ],


    "Development Score":[

        float(selected["DevelopmentScore"]),
        float(selected2["DevelopmentScore"])

    ]

})



fig5 = px.bar(

    compare,

    x="District",

    y="Development Score",

    color="District",

    text="Development Score",

    title="Development Score Comparison"

)



fig5.update_layout(

    plot_bgcolor="white",

    paper_bgcolor="white",

    title_x=0.5

)



st.plotly_chart(

    fig5,

    width="stretch"

)



st.divider()



# ==============================
# AI Recommendations
# ==============================


st.header(
    "🤖 AI Development Recommendations"
)



recommendations = []



if float(selected["LiteracyRate"]) < 60:

    recommendations.append(
        "Increase literacy programs and improve school enrollment."
    )



if int(selected["Hospitals"]) < 10:

    recommendations.append(
        "Increase healthcare infrastructure."
    )



if int(selected["Beds"]) < 1000:

    recommendations.append(
        "Expand hospital bed capacity."
    )



if int(selected["PrimarySchools"]) < 800:

    recommendations.append(
        "Increase primary school facilities."
    )



if float(selected["DevelopmentScore"]) < 35:

    recommendations.append(
        "Allocate additional development budget for this district."
    )



if len(recommendations) == 0:

    st.success(
        "This district performs well across available indicators."
    )


else:

    for item in recommendations:

        st.warning(item)



st.divider()



# ==============================
# Export Reports
# ==============================


st.header(
    "📥 Export Reports"
)



left,right = st.columns(2)



with left:


    st.subheader(
        "Professional PDF Report"
    )


    if st.button(
        "📄 Generate PDF Report"
    ):


        filename = create_report(selected)


        with open(filename,"rb") as pdf:


            st.download_button(

                label="⬇ Download PDF",

                data=pdf,

                file_name=filename,

                mime="application/pdf"

            )



with right:


    st.subheader(
        "District CSV Data"
    )


    district_csv = selected.to_frame().T



    csv = district_csv.to_csv(

        index=False

    ).encode("utf-8")



    st.download_button(

        label="⬇ Download CSV",

        data=csv,

        file_name=f"{selected['District']}_Data.csv",

        mime="text/csv"

    )



st.divider()



# ==============================
# About
# ==============================


st.header(
    "ℹ About Dashboard"
)



about1,about2 = st.columns(2)



with about1:

    st.info(
"""
Dashboard Purpose

This system supports evidence based
development planning for Punjab.

It provides district comparison using
education, health, infrastructure and
demographic indicators.
"""
    )



with about2:

    st.success(
"""
Data Sources

• Punjab Census 2023

• Punjab Development Statistics

• Punjab Health Statistics 2024

• Punjab Education Statistics
"""
    )



st.divider()

st.divider()

# ==============================
# Feedback & Review
# ==============================

st.header("💬 Feedback & Review")

st.markdown("""
Your feedback helps improve the Punjab District Development Dashboard.

We welcome suggestions, reviews, and comments from students, researchers, teachers, planners, and other users.

Your feedback helps us improve dashboard usability, data presentation, and future development features.
""")

st.info("""
⭐ You can share:

• Overall experience
• Suggestions for improvement
• New features ideas
• Data or visualization issues
• Dashboard usability feedback

Your valuable feedback will be reviewed for future updates.
""")

st.link_button(
    "📝 Submit Your Feedback",
    "https://docs.google.com/forms/d/e/1FAIpQLSc33EwYW87sBSgdizVy0_eumoBv1eI4yS3UkEhKcMCcFTG-FA/viewform?usp=sharing&ouid=104802203602457563157"
)

st.caption(
    "Thank you for supporting evidence based development planning."
)

# ==============================
# Credits Footer
# ==============================


st.markdown(
"""
<div style="
background:#145A32;
padding:20px;
border-radius:12px;
text-align:center;
color:white;
">

<h3>
Punjab District Development Dashboard
</h3>

Planning & Development Department

Government of Punjab

<br><br>

Developed by <b>AIZAL STUDIO</b>

<br>

Python | Streamlit | Plotly | Pandas | ReportLab

<br><br>

© 2026

</div>
""",
unsafe_allow_html=True
)