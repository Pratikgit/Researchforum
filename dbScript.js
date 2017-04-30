/* To execute this db script, run command: "mongo < dbScript.js" from an appropriate folder */

//Dropping if Database exists with the same name and create new
use RESEARCH_FORUM_DB
db.dropDatabase()
use RESEARCH_FORUM_DB

//Creating the required collections
db.createCollection("Tags")
db.createCollection("User")
db.createCollection("Paper")
db.createCollection("Summary")
db.createCollection("Comments")

//Inserting documents into Tags collection
db.Tags.insert({domain_name:"Computer Networks"})
db.Tags.insert({domain_name:"Operating Systems"})
db.Tags.insert({domain_name:"Computer Graphics"})
db.Tags.insert({domain_name:"Human Computer Interaction"})
db.Tags.insert({domain_name:"Distributed Systems"})
db.Tags.insert({domain_name:"Machine Learning"})
db.Tags.insert({domain_name:"Natural Language Processing"})
db.Tags.insert({domain_name:"Data Science"})
db.Tags.insert({domain_name:"Artificial Intelligence"})

//Inserting documents into User collection
db.User.insert({name:"vineet", email_id:"vineet@umbc.edu", password:"vineet", university:"UMBC", occupation:"student", tag_ids:"5904ea85c22f39ad539c7986, 5904f41f10827fb110b182db"})
db.User.insert({name:"mayur", email_id:"mayur@umbc.edu", password:"mayur", university:"UMBC", occupation:"student", tag_ids:"5904f43210827fb110b182df, 5904f42410827fb110b182dc"})
db.User.insert({name:"vishal", email_id:"vishal@umbc.edu", password:"vishal", university:"UMBC", occupation:"student", tag_ids:"5904ea85c22f39ad539c7986, 5904f43b10827fb110b182e0"})
db.User.insert({name:"pratik", email_id:"pratik@umbc.edu", password:"pratik", university:"UMBC", occupation:"student", tag_ids:"5904ea85c22f39ad539c7986, 5904f42e10827fb110b182de, 5904f41f10827fb110b182db"})
db.User.insert({name:"abhijeet", email_id:"abhijeet@umbc.edu", password:"abhijeet", university:"ASU", occupation:"student", tag_ids:"5904f42e10827fb110b182de, 5904ea92c22f39ad539c7987"})
db.User.insert({name:"john", email_id:"john@umbc.edu", password:"john", university:"ASU", occupation:"student", tag_ids:"5904ea92c22f39ad539c7987"})
db.User.insert({name:"jeena", email_id:"jeena@umbc.edu", password:"jeena", university:"UCLA", occupation:"student", tag_ids:"5904f43210827fb110b182df"})
db.User.insert({name:"priya", email_id:"priya@umbc.edu", password:"priya", university:"CMU", occupation:"student", tag_ids:"5904ea9cc22f39ad539c7988, 5904ea85c22f39ad539c7986"})
db.User.insert({name:"naveen", email_id:"naveen@umbc.edu", password:"naveen", university:"SJSU", occupation:"student", tag_ids:"5904f43b10827fb110b182e0"})
db.User.insert({name:"pranav", email_id:"pranav@umbc.edu", password:"pranav", university:"NYU", occupation:"student", tag_ids:"5904ea9cc22f39ad539c7988"})

//Inserting documents into Paper collection
db.Paper.insert({title:"Content Caching and Distribution in Smart Grid Enabled Wireless Networks", authors:"Nirwan Ansari, Xueqing Huang", conference:"IEEE Internet of Things", publication_date:"2010-03-29", url:"http://ieeexplore.ieee.org/document/7486055/", tag_ids:"5904ea85c22f39ad539c7986"})
db.Paper.insert({title:"Evaluation of operating systems requirements for safe Wireless Sensor Networks", authors:"Massimiliano Ruggeri, Michele Selvatici", conference:"IECON 2016", publication_date:"2016-10-26", url:"http://ieeexplore.ieee.org/document/7793526/", tag_ids:"5904ea85c22f39ad539c7986, 5904ea92c22f39ad539c7987"})
db.Paper.insert({title:"Application of machine learning techniques to sentiment analysis", authors:"Anuja P Jain, Padma Dandannavar", conference:"Applied and Theoretical Computing and Communication Technology (iCATccT)", publication_date:"2016-07-23", url:"http://ieeexplore.ieee.org/document/7912076/", tag_ids:"5904f42910827fb110b182dd"})
db.Paper.insert({title:"Socio-Demographic Factors and Data Science Methodologies in Type 2 Diabetes Mellitus Analysis", authors:"Diana Canales, Neil Hernandez-Gress", conference:"2016 International Conference on Computational Science and Computational Intelligence (CSCI)", publication_date:"2017-03-20", url:"http://ieeexplore.ieee.org/document/7486055/", tag_ids:"5904f43210827fb110b182df"})
db.Paper.insert({title:"Analysis and proposal of a novel approach to collision detection and avoidance between moving objects using artificial intelligence", authors:"Seema Rawat, Zohaib A. Faridi, Praveen Kumar", conference:"2016 International Conference System Modeling & Advancement in Research Trends (SMART)", publication_date:"2016-11-27", url:"http://ieeexplore.ieee.org/document/7894505/", tag_ids:"5904f43b10827fb110b182e0"})
db.Paper.insert({title:"Batch scheduling model for distributed systems", authors:"Taj Alam, Zahid Raza", conference:"2016 Fourth International Conference on Parallel, Distributed and Grid Computing (PDGC)", publication_date:"2016-12-24", url:"http://ieeexplore.ieee.org/document/7913119/", tag_ids:"5904f42410827fb110b182dc"})
db.Paper.insert({title:"Scalable mental health analysis in the clinical whitespace via natural language processing", authors:"Glen Coppersmith, Casey Hilland, Ophir Frieder, Ryan Leary", conference:"2017 IEEE EMBS International Conference on Biomedical & Health Informatics (BHI)", publication_date:"2017-02-19", url:"http://ieeexplore.ieee.org/document/7897288/", tag_ids:"5904f42e10827fb110b182de"})
db.Paper.insert({title:"Application of the Montessori method in tercial education of a computer 3D graphics", authors:"Josef Brozek, Dan Hamernik, Petr Vesely, Vaclav Svoboda", conference:"2016 ELEKTRO", publication_date:"2016-05-18", url:"http://ieeexplore.ieee.org/document/7512162/", tag_ids:"5904ea9cc22f39ad539c7988"})
db.Paper.insert({title:"Routing in hexagonal computer networks: How to present paths by Bloom filters without false positives", authors:"Gökçe Çaylak Kayaturan, Alexei Vernitski", conference:"2016 8th Computer Science and Electronic Engineering (CEEC)", publication_date:"2016-09-30", url:"http://ieeexplore.ieee.org/document/7835895/", tag_ids:"5904ea85c22f39ad539c7986"})
db.Paper.insert({title:"Quantitative and Qualitative Analysis of Current Data Science Programs from Perspective of Data Science Competence Groups and Framework", authors:"Tomasz Wiktorski, Yuri Demchenko, Adam Belloum, Anoosheh Shirazi", conference:"2016 IEEE International Conference on Cloud Computing Technology and Science (CloudCom)", publication_date:"2016-12-15", url:"http://ieeexplore.ieee.org/document/7830750/", tag_ids:"5904f43210827fb110b182df"})

//Inserting documents into Summary collection
db.Summary.insert({contents:"The distributive caching, green energy sharing, and the on-grid energy backup have improved the reliability and performance of the wireless multimedia downloading process.", user_id:"5904dd93c22f39ad539c797f", paper_id:"5905018e8b49e137b0c66240", time:new Date(), comments:"5904ed49c22f39ad539c798a", upvote:"5"})
db.Summary.insert({contents:"Usually it happens through reuse or renaming and can result in curricula that lack proper balance of competences, which balance is necessary for future data scientists. Our quantitative analysis of over 300 programs worldwide shows that at least one of the three core data science competence groups is under-represented in the majority of programs. Moreover, general business courses are often suggested to students to cover the domain competence group, which in most cases results in superficial treatment of this competence group.", user_id:"5904f7cc7a9eb230da708369", paper_id:"590501e48b49e137b0c66247", time:new Date(), comments:"5904ed49c22f39ad539c798a", upvote:"11"})
db.Summary.insert({contents:"We will be using the A* algorithm to stay away from collisions by path finding and characterize another way to deal with collision avoidance that can be utilized as a part of constant situations by finding all practical collision types. The path finding techniques being used at present turn a blind eye to the sideswipe collisions.", user_id:"5904f8067a9eb230da708370", paper_id:"590501b18b49e137b0c66244", time:new Date(), comments:"5904ed49c22f39ad539c798a", upvote:"1"})
db.Summary.insert({contents:"The objective of this paper is to give step-by-step detail about the process of sentiment analysis on twitter data using machine learning. This paper also provides details of proposed approach for sentiment analysis. This work proposes a Text analysis framework for twitter data using Apache spark and hence is more flexible, fast and scalable. Naïve Bayes and Decision trees machine learning algorithms are used for sentiment analysis in the proposed framework.", user_id:"5904f7e07a9eb230da70836b", paper_id:"590501a08b49e137b0c66242", time:new Date(), comments:"5904ed49c22f39ad539c798a", upvote:"3"})
db.Summary.insert({contents:"Currently available operating systems for applications in the Internet of Things (IoT) domain have different requirements from traditional safety-related applications. With the increasing trend to develop WSN-enabled applications also in the industrial domain and, in general, in human-safety related applications, it is mandatory to assess whether existing systems can be adapted to different application domains, and to estimate the degree of this effort.", user_id:"5904f7cc7a9eb230da708369", paper_id:"590501978b49e137b0c66241", time:new Date(), comments:"5904ed49c22f39ad539c798a", upvote:"9"})
db.Summary.insert({contents:"We construct the Bloom filters for a complicated routing structure in a hexagonal mesh. It is aimed to obtain a fastest scheme without errors. A coding structure for the edges is developed to increase the efficiency use of network resources.", user_id:"5904f7bb7a9eb230da708367", paper_id:"590501dc8b49e137b0c66246", time:new Date(), comments:"5904ed49c22f39ad539c798a", upvote:"5"})
db.Summary.insert({contents:"The distributive caching, green energy sharing, and the on-grid energy backup have improved the reliability and performance of the wireless multimedia downloading process. To minimize the total on-grid power consumption of the whole network, while guaranteeing that each user can retrieve the whole content, the user association scheme is jointly designed with consideration of resource allocation.", user_id:"5904f7ee7a9eb230da70836d", paper_id:"590501a78b49e137b0c66243", time:new Date(), comments:"5904ed49c22f39ad539c798a", upvote:"18"})

//Inserting documents into Comments collection
db.Comments.insert({comment:"Perfectly written!", summary_id:"590523577ed4bf619fa9e457", user_id:"5904f7f67a9eb230da70836e"})
db.Comments.insert({comment:"Could you please explain the networking techniques in brief?", summary_id:"5905234f7ed4bf619fa9e456", user_id:"5904f7d87a9eb230da70836a"})
db.Comments.insert({comment:"I agree with the mentioned description", summary_id:"590523427ed4bf619fa9e455", user_id:"5904f8067a9eb230da708370"})
db.Comments.insert({comment:"Mentioned analysis of results are incorrect", summary_id:"5905232f7ed4bf619fa9e453", user_id:"5904f7cc7a9eb230da708369"})
db.Comments.insert({comment:"The language used in summary is more complicated than the paper", summary_id:"5905236a7ed4bf619fa9e459", user_id:"5904f7bb7a9eb230da708367"})

//Displaying all the existing collections with their data
db.Tags.find()
db.User.find()
db.Paper.find()
db.Summary.find()
db.Comments.find()



