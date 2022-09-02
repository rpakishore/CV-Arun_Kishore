from tkinter import W
import pandas as pd
import streamlit as st
import os, forallpeople
from PIL import Image
from handcalcs.decorator import handcalc
forallpeople.environment('structural', top_level=True)

# <!-----Classes-------->
class checks:
    def __init__(self):
        self.code = """<table align="center" border="1" cellpadding="1" cellspacing="1" summary="A summary of checks and Utilization %">
            <thead>
                <tr>
                    <th scope="col">Checks</th>
                    <th scope="col">Util</th>
                </tr>
            </thead>
            <tbody>
        """
        self.completed_code = None

    def add_check(self, title, util):

        if type(util) != str:
            if util > 1:
                color = "#ff3333"
            else:
                color = "#00FF00"
            util = round(util*100,1)
            self.code += (f"""<tr><td>{title}</td><td style="text-align: center;"><span style="background-color:{color};">{util}%</span></td></tr>""")

        else:
            if util.lower().strip().startswith('fail'):
                color = "#ff3333"
            else:
                color = "#00FF00"
            self.code += (f"""<tr><td>{title}</td><td style="text-align: center;"><span style="background-color:{color};">{util}</span></td></tr>""")
        self.completed_code = None

    def html(self):
        if not self.completed_code:
            self.completed_code = self.code + "</tbody></table>"
        return self.completed_code

class section:
    def __init__(self):
        self.code_block = []
    
    def add_markdown(self, text):
        self.code_block.append({"markdown":text})
    
    def add_latex(self, latex, prefix=None, suffix=None):
        self.code_block.append({
            "latex": latex,
            "prefix": prefix,
            "suffix": suffix})           

    def add_section_title(self, title, status=None, status_text=""):
        if status == None:
            self.code_block.append({"title_only": title})
        elif status.lower() == "ok":
            self.code_block.append({
                "title_success": title,
                'status_text': status_text})
        else:
            self.code_block.append({
                "title_error": title,
                'status_text': status_text})

    def write_calcs(self):
        for item in self.code_block:
            if "markdown" in item.keys():
                st.markdown(item['markdown'])
            elif "latex" in item.keys():
                if not item['prefix'] and not item['suffix']:
                    st.latex(item['latex'])
                elif item['prefix'] and not item['suffix']:
                    left, right = st.columns([1,2])
                    left.markdown(item['prefix'])
                    right.latex(item['latex'])
                elif not item['prefix'] and item['suffix']:
                    left, right = st.columns([2,1])
                    right.markdown(item['suffix'])
                    left.latex(item['latex'])
                else:
                    left, center ,right = st.columns([1,3,1])
                    left.markdown(item['prefix'])
                    center.latex(item['latex'])
                    right.markdown(item['suffix'])

            elif "title_only" in item.keys():
                st.markdown(item['title_only'])
            elif "title_success" in item.keys():
                left, right = st.columns([2,1])
                with left:
                    st.markdown(item['title_success'])
                with right:
                    st.success(item['status_text'])
            elif "title_error" in item.keys():
                left, right = st.columns([1,1])
                with left:
                    st.markdown(item['title_error'])
                with right:
                    st.error(item['status_text'])

calc_block = section()
check = checks()
check_list = {}
calc_variables = {}

# <!-----Functions------>
def write_vals_to_session_state(vals):
    for item in vals.keys():
        calc_variables[item] = vals[item]

def read_pickle(section):
    if section == 'W':
        return pd.read_pickle(os.path.join('.', 'util', 'W_df.pkl'))

def display_df(df):
    dtest = df.astype(str)
    st.table(dtest)

def display_section_properties(df):
    df = df[df['Section']==st.session_state.section].copy()
    if st.session_state.section_type == 'W':
        columns = {
            'Dsg':'Designation', 
            'D':'Depth', 
            'B': 'Breadth', 
            'T': 'Thickness', 
            'Mass': 'Mass', 
            'A': 'Area'
            }
    with left.expander('Section properties'):
        table = {'Parameter':[], 'Value':[]}
        for key, val in columns.items():
            table['Parameter'].append(val)
            table['Value'].append(df[key].values[0])
        display_df(pd.DataFrame(table))

st.header("Base Plate Design")
st.subheader("Inputs")
left, right = st.columns(2)

left.selectbox(
    label="Section Type",
    options=('W', 'HSS'),
    key='section_type'
)

df = read_pickle(st.session_state.section_type)

if st.session_state.section_type == 'W':
    left.selectbox(
        label="Section Size",
        options=df['Section'].to_list()[::-1],
        key="section"
    )
    right.image(Image.open(os.path.join('.', 'assets', 'Anchors_W-section.png')))
    df = df[df['Section']==st.session_state.section].copy()
    st.session_state.section_l = df['D'].values[0]
    st.session_state.section_b = df['B'].values[0]

display_section_properties(df)
st.write(st.session_state.section_l)

left.number_input(
    label="Length of baseplate (L | mm)",
    min_value=st.session_state.section_l / mm,
    key="L"
)
left.number_input(
    label="Width of baseplate (B | mm)",
    min_value=st.session_state.section_b / mm,
    key="B"
)
left.number_input(
    label="Nearest conc. edge dist. from minor axis (Xe | mm)",
    min_value=100,
    key="Xe"
)
left.number_input(
    label="Nearest conc. edge dist. from major axis (Ye | mm)",
    min_value=150,
    key="Ye"
)

right.number_input(
    label="Concrete compressive str (f'c | MPa)",
    value=20,
    key='fc'
)
right.number_input(
    label="Rebar yield str (fy | MPa)",
    value=400,
    key='fy'
)
    
# <!-----Calculations------>
## Concrete bearing capacity

@handcalc(precision=1)
def formula(L,B):
    A_baseplate = L*B
    return locals()
latex1, val = formula(st.session_state.L*mm, st.session_state.B*mm)
write_vals_to_session_state(val)
@handcalc(precision=1)
def formula(L,B):
    A_baseplate = L*B
    return locals()
calc_block.add_section_title(
    title="#### Concrete Bearing Strength",
    status="not ok",
    status_text="Required str. exceeds bearing str."
)
calc_block.add_latex(latex= latex1, prefix="Area of baseplate")
calc_block.write_calcs()
