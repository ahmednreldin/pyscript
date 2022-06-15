pipeline{
    agent any 
    stages{
        stage("Build"){
            when{
                expression{
                    BRANCH_NAME == "Dev"
                }
            }
            steps{
                echo "Build stage from Dev Branch"
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