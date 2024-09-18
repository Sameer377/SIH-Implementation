from PromtSearch import isContextMatched
from CreatePDF import generatePDF

conversations =[
    {
        "id": 1,
        "path": "D:\\OneDrive\\Desktop\\raw\\flowC.png",
        "timestamp": "2024-09-15T10:25:00Z",    
        "context": "Rahul and Rohan were discussing ways to transfer money internationally. Rahul shared his experience with using online services, while Rohan mentioned the benefits of using traditional banking methods. They weighed the pros and cons of each option, considering factors like fees, exchange rates, and security."
    },
    {
        "id": 2,
        "path": "D:\\OneDrive\\Desktop\\raw\\googlelogo.png",
        "timestamp": "2024-09-15T11:00:00Z",
        "context": "Detective James was interviewing a suspect, Alex, about a recent burglary. Alex claimed to have been at a friend's house at the time of the crime, but James noticed inconsistencies in his alibi. The conversation turned tense as James pressed Alex for more information."
    },
    {
        "id": 3,
        "path": "D:\\OneDrive\\Desktop\\raw\\log file creation.png",
        "timestamp": "2024-09-15T12:30:00Z",
        "context": "Samantha and Michael were planning a trip to Paris. They discussed the best time to visit, must-see attractions, and how to navigate the city. Samantha shared her experience with booking accommodations through a travel app, while Michael recommended trying local cuisine."
    },
    {
        "id": 4,
        "path": "D:\\OneDrive\\Desktop\\raw\\loginPage_Img.jpeg",
        "timestamp": "2024-09-15T14:00:00Z",
        "context": "Counselor Rachel was meeting with a victim of domestic abuse, Emily. Rachel listened attentively as Emily shared her story, offering words of comfort and support. They discussed the importance of seeking help and the resources available to Emily."
    },
    {
        "id": 5,
        "path": "D:\\OneDrive\\Desktop\\raw\\phases.png",
        "timestamp": "2024-09-15T15:15:00Z",
        "context": "Lily and Finn were discussing their plans for a road trip across the United States. They debated the best route to take, considering factors like scenic routes, budget, and time constraints. They also talked about the importance of taking breaks and enjoying the journey."
    },
    {
        "id": 6,
        "path": "D:\\OneDrive\\Desktop\\raw\\sameer.jpg",
        "timestamp": "2024-09-15T16:00:00Z",
        "context": "Officer Thompson was speaking with a witness, Jack, about a recent hit-and-run accident. Jack described the vehicle and the driver's behavior, providing crucial details for the investigation. Thompson thanked Jack for his cooperation and assured him that the police would do their best to find the perpetrator."
    },
    {
        "id": 7,
        "path": "D:\\OneDrive\\Desktop\\raw\\Signature .jpg",
        "timestamp": "2024-09-15T17:30:00Z",
        "context": "Dr. Patel was consulting with a patient, David, about his recent diagnosis. David was concerned about the treatment options and the potential side effects. Dr. Patel explained each option in detail, addressing David's concerns and recommending the best course of action."
    },
    {
        "id": 8,
        "path": "D:\\OneDrive\\Desktop\\raw\\usecase.png",
        "timestamp": "2024-09-15T18:45:00Z",
        "context": "A red bus with 14 wheels , 40 students seated inside that bus"
    }
]



filelist = []

context =        input("   Enter prompt : ")
matchval = float(input("Enter threshold : "))

for conversation in conversations:

    if isContextMatched(conversation["context"],context,matchval):
        print(f"File ID: {conversation['id']}\nPath: {conversation['path']}")
        filelist.append(conversation["path"])


if(len(filelist)>0):
    print("Generating PDF.....")
    generatePDF(filelist)
else : 
    print("PDF is not generated....")



print("Task Completed....")    