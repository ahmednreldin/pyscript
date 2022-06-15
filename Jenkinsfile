pipeline{
    agent any 
    environment{
        CREDENTIAL = credentials('TEST')
    }
    stages{
        stage("Build"){
            when{
                expression{
                    BRANCH_NAME == "Dev"
                }
            }
            steps{
                echo "Build stage from Dev Branch ${CREDENTIAL}"
            }
        }
        stage("Deployment"){
            when{
                expression{
                    BRANCH_NAME == "Master"
                }
            }
            steps{
                echo "Deployment of the application"
            }
        }
    }
}