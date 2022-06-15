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
    }
}