#   🎬 Serverless Movies API
## Introduction
The Serverless Movies API is a cloud-native project designed to showcase serverless architecture and AWS services. This API provides movie information stored in a NoSQL database, with functionality to filter movies by release year
## Features
- **GetMovies**: Fetch a list of all movies with their details.
- **GetMoviesByYear**: Retrieve movies released in a specific year.
- **Cloud Storage**: Movie cover images hosted on S3.
## Tech Stack
- **AWS DynamoDB**: NoSQL database for movie storage.
- **AWS S3**: Cloud storage for movie cover images.
- **AWS Lambda**: Serverless functions for backend logic.
- **Amazon API Gateway**: Exposes the API endpoints.
- **Python**: Lambda function code.

## Project Architecture

```plaintext
+-----------------+        +---------------+        +-----------------+
|   HTTP Client   | -----> | API Gateway   | -----> | AWS Lambda      |
| (Postman, etc.) |        +---------------+        +-----------------+
+-----------------+                                       |
                                                           v
                                               +-------------------+
                                               | AWS DynamoDB      |
                                               +-------------------+
                                                           |
                                                           v
                                               +-------------------+
                                               | AWS S3 (Images)   |
                                               +-------------------+
```


## API Endpoints
### 1. **GetMovies**
- **Method**: GET
- **Endpoint**: /getmovies
- **Description**: Fetches all movies from the database.
- **Example Response**:
```json
[
    {
        "releaseYear": 2010.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Game+of+thrones.jpg",
        "title": "Game of Thrones"
    },
    {
        "releaseYear": 2009.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Avatar.jpg",
        "title": "Avatar"
    },
    {
        "releaseYear": 2010.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Inception.jpg",
        "title": "Inception"
    },
    {
        "releaseYear": 2022.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Anikulapo.webp",
        "title": "Anikulapo"
    },
    {
        "releaseYear": 2023.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Barbie.jpg",
        "title": "Barbie"
    },
    {
        "releaseYear": 1949.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Samson+%26+Delilah.jpg",
        "title": "Samson and Delilah"
    },
    {
        "releaseYear": 2024.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=The+hitman.jfif",
        "title": "The Hitman"
    },
    {
        "releaseYear": 2013.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Transformers.jpg",
        "title": "Transformers: Age of Extinction"
    },
    {
        "releaseYear": 2024.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=The+substance.jfif",
        "title": "The Substance"
    }
]
```
## 2. **GetMoviesByYear**
- **Method**: GET
- **Endpoint**: /getmoviesbyyear?year=<year>
- **Description**: Fetches movies released in the specified year.
- **Example Request**:
```plaintext
GetMoviesByYear?year=2022
```
- **Example Response**:
```json
[
    {
        "releaseYear": 2022.0,
        "coverURL": "https://us-east-1.console.aws.amazon.com/s3/object/movie-covers-bucket?region=us-east-1&bucketType=general&prefix=Anikulapo.webp",
        "title": "Anikulapo"
    }
]
```
## How to Set Up

### Prerequisites
- **AWS Account**  
- **Python 3.x** installed locally  
- **AWS CLI** configured  

### Steps

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/Funmisho/Serverless-Movies-API.git
   cd Serverless-Movies-API
   
2. **Set Up AWS Resources**
   - Create a DynamoDB Table named `Movies`. 
   - Create an S3 Bucket for storing movie cover images.

3. **Upload Movie Cover Images**
   - Place your movie cover image in the S3 bucket.
   - Note the image URLs and add them to your DynamoDB table under the `coverUrl` field.  

4. **Deploy Lambda Functions**
- Package the Python scripts for Lambda functions.
- Deploy them via the AWS Lambda Console or CLI.
  
5. **Configure API Gateway**
  - Create HTTP APIs for `/getmovies` and `/getmoviesbyyear`.
  - Link the APIs to respective Lambda functions

6. **Test the API**
  - Use Postman or a similar tool to test the endpoints.

## Contributing
Contributions are welcome! For major changes, kindly open an issue first to discuss what you would like to change.

## Credits
- **Author**: Akinmi Oluwabukunmi Funmisho
- **Acknowledgements**: Thanks to @madebygps https://github.com/madebygps for their https://learntocloud guide which was the template for the knowledge to do this project

## License
This project is open source and available under the MIT License.
- 

