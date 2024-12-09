
import streamlit as st
import pandas as pd

# Load regression coefficients
data = {
    "Structure": ["SDFT-TP MRI T1", "DDFT-TP MRI T1", "SDFT-SP MRI T1", "DDFT-SP MRI T1", "WICB-CP MRI T1",
                  "LICB-CP MRI T1", "AML-TP MRI T1", "AML-SP MRI T1", "WACB-SP MRI T1", "LACB-SP MRI T1",
                  "SDFT-TP MRI T2", "DDFT-TP MRI T2", "SDFT-SP MRI T2", "DDFT-SP MRI T2", "AML-TP MRI T2", "AML-SP MRI T2"],
    "BW_int": [1.904, 2.113, 1.447, 1.389, 3.039, 2.721, 1.823, 1.745, 2.193, 1.841, 1.834, 2.195, 1.496, 1.388, 1.794, 1.671],
    "BW_coef": [0.079, 0.075, 0.081, 0.071, 0.159, 0.136, 0.098, 0.083, 0.112, 0.093, 0.078, 0.077, 0.082, 0.074, 0.095, 0.087],
    "CJC_int": [0.871, 1.141, 0.384, 0.434, 1.015, 0.915, 0.829, 0.754, 0.947, 0.884, 0.864, 1.114, 0.394, 0.454, 0.864, 0.804],
    "CJC_coef": [0.022, 0.02, 0.022, 0.02, 0.043, 0.039, 0.025, 0.021, 0.032, 0.028, 0.019, 0.018, 0.021, 0.02, 0.023, 0.022],
    "LDO_int": [1.123, 1.358, 0.63, 0.632, 1.238, 1.127, 1.045, 0.934, 1.102, 1.034, 1.101, 1.35, 0.641, 0.633, 1.145, 1.012],
    "LDO_coef": [0.008, 0.007, 0.008, 0.007, 0.016, 0.014, 0.009, 0.007, 0.01, 0.009, 0.008, 0.007, 0.008, 0.007, 0.009, 0.008],
    "LDCJ_int": [0.709, 0.98, 0.233, 0.346, 0.57, 0.487, 0.409, 0.351, 0.523, 0.465, 0.713, 0.985, 0.24, 0.357, 0.57, 0.505],
    "LDCJ_coef": [0.02, 0.019, 0.021, 0.018, 0.042, 0.037, 0.029, 0.023, 0.032, 0.028, 0.02, 0.018, 0.021, 0.019, 0.023, 0.021],
    "LCJO_int": [1.456, 1.672, 0.978, 0.911, 1.858, 1.724, 1.634, 1.478, 1.801, 1.647, 1.501, 1.684, 1.015, 0.924, 1.813, 1.695],
    "LCJO_coef": [0.011, 0.011, 0.012, 0.011, 0.025, 0.021, 0.017, 0.014, 0.02, 0.016, 0.011, 0.011, 0.012, 0.011, 0.014, 0.013]
}
coefficients = pd.DataFrame(data)

# Apply custom styles for centering and page width
st.markdown(
    '''
    <style>
    .main {
        max-width: 2000px;
        margin: 0 auto;
    }
    .block-container {
        padding-top: 2rem;
    }
    h1, h2 {
        text-align: center;
    }
    table {
        text-align: center;
        margin: 0 auto;
    }
    th, td {
        text-align: center !important;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

st.title("Canine Carpal Joint Structure Estimator")

st.header("Input Measurements")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    BW = st.number_input("BW (kg)", value=0.0)
with col2:
    CJC = st.number_input("CJC (mm)", value=0.0)
with col3:
    LDO = st.number_input("LDO (mm)", value=0.0)
with col4:
    LDCJ = st.number_input("LDCJ (mm)", value=0.0)
with col5:
    LCJO = st.number_input("LCJO (mm)", value=0.0)

# Add description below input
st.markdown("""
### Note:
#### The models were optimized for animals weighing over 10 kg and for non-chondrodystrophic breeds.
""")

# Initialize default table with zeros
results_df = pd.DataFrame(
    {
        "Structure": coefficients["Structure"],
        "Estimated Size (mm) based on BW": [0] * len(coefficients),
        "Estimated Size (mm) based on CJC": [0] * len(coefficients),
        "Estimated Size (mm) based on LDO": [0] * len(coefficients),
        "Estimated Size (mm) based on LDCJ": [0] * len(coefficients),
        "Estimated Size (mm) based on LCJO": [0] * len(coefficients),
    }
)




# Update only the relevant column based on input changes
if BW != 0.0:
    results_df["Estimated Size (mm) based on BW"] = coefficients["BW_int"] + coefficients["BW_coef"] * BW

if CJC != 0.0:
    results_df["Estimated Size (mm) based on CJC"] = coefficients["CJC_int"] + coefficients["CJC_coef"] * CJC

if LDO != 0.0:
    results_df["Estimated Size (mm) based on LDO"] = coefficients["LDO_int"] + coefficients["LDO_coef"] * LDO

if LDCJ != 0.0:
    results_df["Estimated Size (mm) based on LDCJ"] = coefficients["LDCJ_int"] + coefficients["LDCJ_coef"] * LDCJ

if LCJO != 0.0:
    results_df["Estimated Size (mm) based on LCJO"] = coefficients["LCJO_int"] + coefficients["LCJO_coef"] * LCJO

# Display results
st.header("Estimated Internal Structures")
st.table(results_df)

# Add description below input
st.markdown("""
**Descriptions**:
- **BW**: Body Weight  
- **CJC**: Carpal Joint Circumference  
- **LCJO**: Length from Carpal Joint to Olecranon  
- **LDCJ**: Length from Digits to Carpal Joint  
- **LDO**: Length from Digits to Olecranon  
- **TP**: Transverse Plane  
- **SP**: Sagittal Plane  
- **CP**: Coronal Plane  
- **SDFT**: Superficial Digital Flexor Tendon (diameter)  
- **DDFT**: Deep Digital Flexor Tendon (diameter)  
- **AML**: Medial accessory-metacarpal ligament (diameter)  
- **WICB**: Width of Intermedioradial Carpal Bone  
- **LICB**: Length of Intermedioradial Carpal Bone  
""")
