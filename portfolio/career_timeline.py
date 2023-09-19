import streamlit as st
from streamlit_timeline import timeline
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Literal

@dataclass
class Project:
    start_date: datetime
    title: str
    html_description: str
    img_url: str
    category: Literal["Construction Admin", "Design", "Independent Review"]
    img_caption: Optional[str] = ""

    def as_dict(self) -> dict:
        return {
            'start_date': {
                'year': f"{self.start_date.year}",
                'month': f"{self.start_date.month}"
            },
            'text': {
                'headline': self.title,
                'text': self.html_description
            },
            'media': {
                'url': self.img_url,
                'caption': self.img_caption
            },
            'group': self.category
        }


AMLI = Project(
    start_date=datetime(2016,3,1),
    title="AMLI Arts Center",
    html_description="""
    443,000 sq ft | $66 million | 19 stories | LEED BD+C: NC v3 Gold 
    <br><br>
    <b>Structural Features</b>
    <li>Planted landscaping, a structured pool, sundeck, and other luxury amenities are supported on the top level of the parking deck.</li>
    <li>Tower floors typically consist of 7-1/2″ thick post-tensioned flat slabs which minimizes structural depth and allows for reduced overall building height. This provides significant savings on building skin costs, while still allowing for luxury features such as 10 foot ceiling heights and floor-to-ceiling windows. </li>
    <li>The concrete flat slab also allows for the slab soffit to serve as the ceiling in many locations, which provides additional savings.</li>
    <li>The multi-story pedestrian bridge is constructed using concrete-framed structure. This allowed the bridge to be constructed efficiently and simultaneously with the tower.</li>
    """,
    img_url="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/project/AMLI-Arts-Center_Hero.jpg",
    img_caption="uzuncase.com",
    category="Construction Admin"
)

POWELL = Project(
    start_date=datetime(2019,7,1),
    title="Powell River Consolidated WasteWater Treatment Plant",
    html_description="""
    <p>Structural designer for the two structures of the treatment plant, comprising admin building and process building.  </p>
    <p>Materials used for the various building structures include concrete, masonry, steel and wood-frame.  </p>
    <p>The structural design is carefully undertaken to ensure the key requirements of wastewater facilities, such as durability against the aggressive process environment, process and operational needs, post-disaster seismic resistance, and water-tightness of the process cells and channels, are all met.</p>
    """,
    img_url="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/project/Graham-Wastewater-mainweb.jpg",
    img_caption="constructconnect.com",
    category="Design"
)

LOWER_SEYMOUR = Project(
    start_date=datetime(2019,10,1),
    title="Lower Seymour Watershed Admin Building",
    html_description="""
    <p>Design engineer responsible for the foundations of architecturally expressive administration building, consisting of an entry space, office workspaces, a multipurpose area and various rooms.  </p>
    <p>The pitched roof structure will be constructed in cross-laminated timber and will have a number of significant overhangs.</p>
    """,
    img_url="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/project/Lower_Seymore.png",
    img_caption="",
    category="Design"
)

SFU = Project(
    start_date=datetime(2020,12,1),
    title="Simon Fraser University Parcel 21",
    html_description="""
    <p>Situated on Simon Fraser University's Burnaby campus, the Parcel 21 energy-efficient residence will house over 80 affordable rental apartment units. It comprises a four-storey wood frame building on a concrete parkade, plus a six-storey wood frame building. Associated Engineering was retained to provide structural and electrical engineering services on this $21.5 million project.</p>
    <p>To meet the rigorous BC Energy Step Code requirements, we applied many passive house principles in the design of the project, including:
        <li>A super-insulated building envelope</li>
        <li>Continuous air barrier to minimize leakage</li>
        <li>High performance windows</li>
        <li>Engineering and detailing of connections details to minimize thermal bridging</li>
        <li>A heat-recovery ventilation system to improve indoor air quality</li>
        <li>Canopies and other structures that are thermally separated from the building envelope</li>
        <li>Sunshades that help prevent overheating in the summer</li>
    </p>
    <p>In addition to designing the structure for high seismicity, the structural detailing was carefully undertaken to mitigate the effects of vertical shrinkage of the wood structure and to preserve the continuity of the thermal envelope around the residential portion of the structure.</p>
    """,
    img_url="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/project/sfu-parcel-21---image-3.jpg",
    img_caption="ae.ca",
    category="Construction Admin"
)

SERPENTINE = Project(
    start_date=datetime(2022,2,1),
    title="Serpentine Water Control Structure",
    html_description="""
    Watertight concrete structure spanning acorss the serpentine river whose: 
    <li>Primary purpose is to provide flood protection to the Surrey Lowlands</li>
    <li>Limits the tidal fluctuation in the Serpentine River.</li>
    <li>Allows the Serpentine River to flow into Boundary Bay through gravity drainage during periods of low tide.</li>
    <li>Intent is to replace the existing structure which is over 100 years old, seismically vulnerable, and cannot accommodate future sea level rise.</li>
    """,
    img_url="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/project/Serpentine.png",
    img_caption="",
    category="Design"
)





PROJECT_LIST = [AMLI, POWELL, SERPENTINE, LOWER_SEYMOUR, SFU]
def get_projects(project_list: list[Project]) -> list[dict]:
    return [project.as_dict() for project in project_list]

def main():
    st.subheader('Career snapshot')
    with st.spinner(text="Building line"):
        timeline_path = Path(__file__).parent / "timeline.json"
        with open(timeline_path, "r", encoding="utf-8") as f:
            data = f.read()
        data = {'events': get_projects(PROJECT_LIST)}
        timeline(data, height=900)
        
    st.markdown("""---""") 