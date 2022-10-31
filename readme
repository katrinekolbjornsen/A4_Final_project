# A3_Use_Case
## 3A: Analyse use case

### Goal: Goal of the tool / workflow in one sentence. i.e. to support the user to calculate the total total cost of the project.
This use case extracts the volume of concrete in IFC-models, which can be used to determine e.g. cost, carbon footprint and the amount demanded from the manufacturer. 


### Model Use (Bim Uses): Please refer initially to the Mapping BIM uses, use cases and processes section in this document.
The IFC model is being analysed using blender bim (or another compatable software) to extract the necessary information and geometry which is further used to calculate the totale volume of concrete. 




## 3B: Propose a (design for a) tool / workflow
### Process: model the process diagram from your use case in BPMN.io please remember to save the .bpmn file and you can save a .svg file that you can insert into your report. 
#### Description of the process of your tool / workflow.
- The process begins with importing the IFC-model. 
- The script searches through the model and finds the elements that are defined as structural elements.
- If no structural element is found, the process starts over again and a new file is requested. 
- Further, the elements defined with the material "concrete" are extracted along with their dimensions and geometry data. 
- Among the concrete elements the script finds the beams, columns, slabs and walls. 
- The concrete volume of each individual type is calculated and put into a list. 
- The volumes of each type are summarized. 
- A list then presents the volume for all the types. 
- A complete volume for all the structural elements in the model is then created. 




## 3C: Information exchange
### Information Exchange: Fill out the excel template with the information for your planned tool / workflow. For this you will need access to the excel, and the Dikon document to help you specify the LOD (LOR,LOG,LOI) for each element you need for you tool / workflow. This can get confusing - don’t worry we can help. 
All the sections that are relevant for structural elements in concrete has been filled out in the Excel-sheet. Mainly LOD 300 DK, which contains "Molio Level of information 4" giving the defined geometry. "The LOD levels include a predefined set of matching levels for LOR, LOG and LOI" (DiKon-BIM7AA_Molio_Construction_Element_Specifications). Meaning that the LOR, LOG and LOI are defined along with the LOD. See example below:

LOR 300: 'DEFINED'
LOG 300: 'TYPE-LEVEL'
LOI 300: 'PROPERTIES FOR SERVICE' - Classification: Classification code, Type (-code/-ID). Digital Design: Type Name, Geometry.


### IFC: Describe the IFC entities and properties for each of the elements you identified in your information exchange.
#### Describe the data that you need to find in the IFC
The data needed in the IFC is:
- IFC space
- IFC building element
- IFC beam
- IFC column
- IFC slab
- IFC wall
- IFC material
- IFC geometry 
- IFC name
- IFC type 


#### Describe the data that you need to find in an external sources i.e. BR18. Based on assumptions (useful when we don't have the 'real' data that we need for our tool)
As far as we can tell there is no need for external sources at this point. 




## 3D: Value: What is the potential improvement offered by this tool?
### This is the common question when developing tools and processes as an intrapreneur in a company. You should consider the business and societal value of this tool – does it save time to the company, does it make employees happier / more productive? Could it reduce material use in society?

It saves time because there is no requirement to knowing a modelling program beforehand. 
Ususally a structural engineer would use a program to create a list for the manufacturers, but with this script anyone in the company could extract that information. 
It could also help developers and architects to consider the fraction of concrete used in the design. 
The script can also calculate the carbon footprint of the building. 
This procedure can also be implemented for other materials and buildings. 
This results as a useful tool for the LCA and cost analysis. 
The possibilies are endless. 


### Describe the business value (How does it create value for your business / employer)
The script makes value by saving time and making the process of extrating information from the building easy and quick.
It also does not require a large expertise within modelling and computering. 


### Describe the societal value (How does it make the world better). N.B. If it doesn't do either of these things (ideally it should do both - don't do it!!)
Since it is easy to extract the total volume of concrete in the building, this can be used in the future as a measurement of the ratio of concrete used in a structure. E.g. If the ratio is set to be no more than 40% due to carbon footprint, the script could easily be used to measure if the building is within the limit. 




## 3E: Delivery
### In this assignment we will focus on the input data that you need for your final tool / workflow. 


#### 9. Your tool/workflow: Description of how your tool / workflow would solve the use case 
The use case is solved creating a Python script in the BlenderBim add-on. Using an open IFC platform makes it accessable for users with limited resources. 


#### 10. Delivery: Description of how you would make the tool / workflow - what steps would you go through?
The Python script would be created by first going through the process of calculating the volume of structural elements.
Based on that, the information that is needed can be listed. The method on how to extract the information must then be discussed, and looking into the IFC classes.
As the properties of the elements is extracted, the script must be developed to be user friendly and give continous information to the user.
Blender will be used to investigate the IFC-model to understand its structure, making it easier to create the script.
