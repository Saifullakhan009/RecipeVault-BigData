# 🌟 BigData Recipe Management System

## 🍔 Overview
The **BigData Recipe Management System** is a scalable, cloud-integrated platform for managing a large dataset of recipes. It allows users to **upload, view, and interact** with recipes efficiently by leveraging **MongoDB, Amazon DynamoDB, and Amazon S3** alongside a **Flask API** for smooth data handling.

## 📅 Features
- **🍲 Add Recipe**: Users can add new recipes, including name, ingredients, instructions, and images.
- **📝 View Recipes**: Fetch and display stored recipes.
- **🖼️ Upload Images**: Store recipe images securely on **Amazon S3**.
- **✅ Interaction Tracking**: Track views and likes using **MongoDB**.
- **👁️ Metadata Management**: Store and retrieve metadata such as views, likes, and tags using **DynamoDB**.
![image](https://github.com/user-attachments/assets/1c21b2bf-3fed-490e-8234-20defafa4662)

---

## 📊 Architecture
### 🏢 System Workflow
1. **User requests** to add/view a recipe.
2. **Flask API** processes the request and interacts with the databases.
3. Recipe **data is stored in MongoDB**.
4. Recipe **images are uploaded to Amazon S3**.
5. **Metadata (views, likes) is recorded in DynamoDB**.
6. **System returns a response** to the user.

### 🗃️ Data Storage and Management
| Component    | Purpose |
|-------------|---------|
| **MongoDB** | Stores recipe details (ingredients, instructions, names) |
| **Amazon S3** | Stores images associated with recipes |
| **DynamoDB** | Stores metadata (views, likes, tags) |

---

## 📝 Technology Stack
### 📊 MongoDB (Recipe Details)
💡 **Description**: MongoDB is a NoSQL database designed for flexibility and scalability.
- **Best for:** Storing JSON-like recipe documents.
- **Why MongoDB?**
  - Schema-less structure allows dynamic fields.
  - Ideal for hierarchical data (recipes with ingredients, instructions).
  - Fast read/write operations.

#### 💪 Commands:
```bash
# Start MongoDB
mongod --dbpath /data/db

# Insert a Recipe Document
mongo
> use recipesDB
> db.recipes.insertOne({ "name": "Pasta", "ingredients": "Tomatoes, Basil, Olive Oil", "instructions": "Boil pasta and mix." })

# Fetch All Recipes
db.recipes.find().pretty()
```

### 🏢 Amazon S3 (Image Storage)
💡 **Description**: Amazon S3 is a scalable cloud storage for objects like images and files.
- **Best for:** Storing large media files securely.
- **Why S3?**
  - Highly durable and scalable.
  - Supports automatic backups and versioning.

#### 💪 Commands:
```bash
# Upload an Image
aws s3 cp my_recipe.jpg s3://my-recipe-bucket/

# List Files in S3 Bucket
aws s3 ls s3://my-recipe-bucket/
```

### 🔢 Amazon DynamoDB (Metadata Storage)
💡 **Description**: Amazon DynamoDB is a NoSQL database optimized for key-value and document storage.
- **Best for:** Handling **recipe metadata (views, likes, tags)**.
- **Why DynamoDB?**
  - High-speed read/write for frequently updated metadata.
  - Auto-scaling capabilities.

#### 💪 Commands:
```bash
# Create a Table
aws dynamodb create-table --table-name RecipeMetadata --attribute-definitions AttributeName=recipe_id,AttributeType=S --key-schema AttributeName=recipe_id,KeyType=HASH --billing-mode PAY_PER_REQUEST

# Insert Metadata
aws dynamodb put-item --table-name RecipeMetadata --item '{"recipe_id": {"S": "1"}, "views": {"N": "10"}, "likes": {"N": "5"}}'

# Fetch Metadata
aws dynamodb get-item --table-name RecipeMetadata --key '{"recipe_id": {"S": "1"}}'
```

---

## 🗂 API Endpoints
### 👨‍💻 User Interaction
#### 🔄 Fetch Recipes
```bash
curl -X GET http://127.0.0.1:5000/get_recipes
```
#### 🍽️ Add Recipe
```bash
curl -X POST http://127.0.0.1:5000/add_recipe -H "Content-Type: application/json" -d '{"recipe_id": "2", "name": "Spaghetti Bolognese", "ingredients": "Spaghetti, Beef, Tomato Sauce", "instructions": "Cook pasta, make sauce, mix.", "image_url": "s3://my-recipe-bucket/spaghetti.jpg"}'
```
#### 🖼️ Upload Image
```bash
curl -X POST -F "file=@/path/to/image.jpg" http://127.0.0.1:5000/upload_file
```

---

## 🔧 Design Challenges
- **📈 Handling Large Data Volumes**: Efficiently managing large recipe datasets.
- **⚖️ Data Consistency**: Synchronizing MongoDB, DynamoDB, and S3.
- **🏢 Cloud Integration**: Ensuring smooth AWS service interactions.
- **🚀 Scalability**: Supporting increasing user requests and uploads.
- **🌐 Performance Optimization**: Reducing query latency and improving response times.


---

# 🌐 System Architecture and Flow

This section outlines the system architecture and interaction flow within the application, which integrates **Flask API**, **MongoDB**, **DynamoDB**, and **Amazon S3** to handle recipe management, image uploading, and metadata processing. Below are key diagrams that demonstrate the processes involved in adding recipes, managing images, and retrieving data.
![image](https://github.com/user-attachments/assets/fbbb087d-e4b3-42b4-b569-c9c2baaf3821)

---

## 1. 🧑‍🍳 User Interaction Flow

### **Figure 1: User Interaction Flow** ✨

This flowchart illustrates the sequence of user actions within the application. It highlights the interaction between the **User** 🧑‍🍳, **Flask API** 🔧, **MongoDB** 🗃️, **DynamoDB** 💾, and **Amazon S3** ☁️ for tasks such as adding or viewing recipes 🍲, uploading images 📸, and interacting with recipe metadata (e.g., views 👁️ and likes ❤️). The flow provides a clear visualization of how the user interfaces with the system.

![image](https://github.com/user-attachments/assets/617867d4-bcdd-435c-a742-ccdf02051196)

---

## 2. 🏗️ System Architecture Overview

### **Figure 2: System Architecture for Data Storage and Retrieval** 🔄

This diagram represents the overall architecture of the system. It demonstrates the relationship between **MongoDB** 🗃️, **DynamoDB** 💾, and **Amazon S3** ☁️ for storing and retrieving data, as well as the role of **Flask API** 🔧 in facilitating user interactions with these storage services. The diagram showcases how each component contributes to the functioning of the application.

![image](https://github.com/user-attachments/assets/c765483b-8ed4-4c2f-9a4d-7aefb2b356af)

---

## 3. 🍴 Recipe Addition and Image Upload Process

### **Figure 3: Sequence Diagram for Adding a Recipe** 📈

This sequence diagram details the process involved in adding a new recipe to the system. It includes the steps of uploading images 📸 to **Amazon S3** ☁️, saving the recipe information (e.g., ingredients 🥘, steps 📝) in **MongoDB** 🗃️, storing metadata (such as views 👁️ and likes ❤️) in **DynamoDB** 💾, and confirming the addition ✅ to the user. This diagram visually captures the flow of data as the user adds new recipes.
![image](https://github.com/user-attachments/assets/446c6200-58ab-452e-b299-4e29ca4a2633)


---

## 📚 Conclusion

The diagrams provided above offer a comprehensive view of how the system handles user interactions, stores and retrieves data, and manages the recipe addition process. They serve as a crucial reference for understanding the internal workflow and architectural design of the application.

---


## 🏆 Contributors
This project was developed by Hajra Nisar, Bushra Shahbaz, and Fatima Najam, who managed different aspects of the system, including backend development, cloud infrastructure, and frontend design. To facilitate local execution, LocalStack was used, which provides a fully functional local AWS cloud environment. This allowed us to test and integrate AWS services like S3 and DynamoDB without deploying to the actual cloud.

Hajra Nisar - [GitHub](https://github.com/hajragit)

Bushra Shahbaz - [GitHub](https://github.com/Bushra-Butt-17)

Fatima Najam - [GitHub](https://github.com/najamfatim)

---

💪 *Happy Coding!* 💪

