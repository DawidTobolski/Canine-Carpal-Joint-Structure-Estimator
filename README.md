
# Canine Carpal Joint Structure Estimator

This repository hosts a Streamlit application designed to estimate the physiological dimensions of canine carpal joint (CCJ) structures based on simple external measurements. This tool bridges the gap between complex imaging modalities and accessible diagnostics, enabling veterinarians and researchers to obtain predictive anatomical insights with ease.

## **Background**
Canine carpal joint disorders are significant in veterinary orthopedics, requiring precise imaging for diagnosis. Advanced modalities like MRI and USG have enhanced diagnostic accuracy, but they remain resource-intensive. This app employs mathematical regression models derived from a study involving MRI, USG, and radiographic imaging to predict internal CCJ dimensions based on external measurements, offering a non-invasive, cost-effective alternative.

## **App Features**
- **Input Measurements**: Users can enter five key measurements:
  - **BW**: Body Weight (kg)
  - **CJC**: Carpal Joint Circumference (mm)
  - **LDO**: Length from Digits to Olecranon (mm)
  - **LDCJ**: Length from Digits to Carpal Joint (mm)
  - **LCJO**: Length from Carpal Joint to Olecranon (mm)
- **Predictive Outputs**:
  - Estimated sizes of internal structures such as:
    - **SDFT**: Diameter of Superficial Digital Flexor Tendon (mm)
    - **DDFT**: Diameter of Deep Digital Flexor Tendon (mm)
    - **AML**: Diameter of Medial Accessory-Metacarpal Ligament (mm)
    - **WICB**: Width of Intermedioradial Carpal Bone (mm)
    - **LICB**: Length of Intermedioradial Carpal Bone (mm)
- Results are displayed in a clear, interactive table with estimated values for each structure based on the entered measurements.

## **Key Findings from the Study**
- Strong correlations were observed between external measurements (e.g., BW) and internal CCJ dimensions (r > 0.9, p < 0.01).
- MRI measurements showed the highest accuracy and predictive power but were effectively modeled using external metrics.
- The regression models were optimized for dogs weighing over 10 kg and non-chondrodystrophic breeds.

## **How to Use the App**
1. **Run the App Locally**:
   Clone this repository and install the required dependencies:
   ```bash
   git clone https://github.com/DawidTobolski/Canine-Carpal-Joint-Structure-Estimator.git
   cd Canine-Carpal-Joint-Structure-Estimator
   pip install -r requirements.txt
   streamlit run streamlit_app_updated.py
   ```
2. **Deployed App**:
   Access the hosted app on Streamlit Cloud: [Canine Carpal Joint Estimator](https://share.streamlit.io/DawidTobolski/Canine-Carpal-Joint-Structure-Estimator/main/streamlit_app_updated.py)

## **Technical Overview**
- **Models**: Linear regression equations derived from MRI imaging.
- **Languages/Tools**: Python, Streamlit, pandas.
- **Design**: Interactive interface with dynamically updated results based on user inputs.

## **Target Audience**
This tool is designed for veterinarians, researchers, and students in veterinary medicine, particularly those focusing on orthopedic diagnostics.

## **Limitations**
- The app is optimized for non-chondrodystrophic breeds and dogs weighing over 10 kg.
- Predictions may vary for smaller or atypical breeds.

## **Future Directions**
- Expansion to include more breeds and body types.
- Integration with additional imaging modalities for broader applicability.

## **Citations**
If you use this tool in your research or clinical practice, please cite:
- Angelika Tobolska et al. *Mathematical models predict the physiological dimensions of selected canine carpal joint structures across imaging modalities in healthy dogs.*

## **Acknowledgments**
This app was developed based on research supported by the Faculty of Veterinary Medicine, University of Warmia and Mazury, and Warsaw University of Life Sciences.

## **License**
This project is licensed under the MIT License. See `LICENSE` for more details.
