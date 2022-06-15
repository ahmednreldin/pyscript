pipeline{
    agent any 
    stages{
        stage("Build"){
            when{
                expression{
                    BRANCH_NAME == "Dev"
                }
            }
            step{
                echo "Build stage from Dev Branch"
            }
        }
    }
}