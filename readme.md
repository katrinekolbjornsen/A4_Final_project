# A4_Final_Project

### Goal: Goal of the tool / workflow in one sentence. i.e. to support the user to calculate the total total cost of the project.
This use case helps the structural engineer to control the structural elements in an IFC-model, by checking that the elements' materials are classified.


### Model Use (Bim Uses): Please refer initially to the Mapping BIM uses, use cases and processes section in this document.
The IFC model has been analysed by blender bim and excel. Blender bim was mainly used as a visual tool, that also somewhat illustrated the structure of the model in the sidebar. The excel file corresponding to the model was a more detailed and explantiory tool, where the structure of the model was illustrated in a different way. Both blender bim and excel was used to retrive information about the structure of the model and how it is divided into different objects, elements etc. 
After learning the structure of the model, a Python script was developed to extract the necessary information to develop a feedback-returning Python script that would assist the structural engineer when making their controls of the model. 


## 3B: Propose a (design for a) tool / workflow
### Process: model the process diagram from your use case in BPMN.io please remember to save the .bpmn file and you can save a .svg file that you can insert into your report. 
#### Description of the process of your tool / workflow.
- The process begins with importing the IFC-model. 
- The script searches through the model and finds the elements that are defined as structural elements.
- If no structural elements are found, the process starts over again and a new file is requested.
- The script finds the structural elements that are classified as beams, columns, slabs, and walls.
- When the structural elements that are found do not have a specified material, a warning is presented.The warning states which element lacks material data.
- The warning encourages the engineer to change the material data in their chosen programme (e.g. Revit).
- After the changes are complete, the updated file can be controlled again.


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
The tool helps the structural engineers to define the material properties of the structural elements correctly, making it easier to extract important information from the IFC-file. With a "clean" IFC-file the cost calculations, life cycle assessment, carbon footprint etc., can be extracted by other parties of the project. The tool therefore opens up many possibilites for using BIM interactively in a company. 


### Describe the business value (How does it create value for your business / employer)
The tool helps the company's engineers to create models that are correctly defined and classified, opening up the possibilities of other disciplinaries to use the IFC-model. When the engineers have a better understanding and practice of how to define the properties in the structural model, time and other resources are saved for the business. It is always important that the engineers perform a quality control of their own work, which the tool helps them to complete by creating a routine of control.  

Another valuable aspect of the project, is that it is possible to perform using other coding languages and open BIM tools, such as Java and Speckle. The tool is a good starting point for other future work. An idea is to create a script that together with a 3D illustrator can highlight the structural object which needs a material defined. The script can also be further developed to control other aspects of the model, for example the classification of each object in the file, and other attributes. This makes the project highly flexible if the employees have experiences with different languages and programs.

### Describe the societal value (How does it make the world better). N.B. If it doesn't do either of these things (ideally it should do both - don't do it!!)
By creating better and more defined models it creates value for all participants in the project, as it is easier to extract information and by that creating a more effetive project process. In the big picture, better models helps the society in a way that the government officials and government-owned projects excecute their work more efficiently and economically. 


## 3E: Delivery
### In this assignment we will focus on the input data that you need for your final tool / workflow. 


#### 9. Your tool/workflow: Description of how your tool / workflow would solve the use case 
The use case is solved creating a Python script in the BlenderBim add-on. Using an open IFC platform makes it accessable for users with limited resources. 


#### 10. Delivery: Description of how you would make the tool / workflow - what steps would you go through?
The Python script would be created by first going through the structural elements.
Based on that, the information that is needed can be listed (i.e. investigate beams, columns, slabs, etc.). The method on how to extract the information must then be discussed, and looking into the IFC classes.
As the properties of the elements is extracted (or cannot be extracted), the script must be developed to be user friendly and give continous information to the user.
Blender will be used to investigate the IFC-model to understand its structure, making it easier to create the script.
