pipeline{
    agent any 
    stages{
        stage("Build"){
            when{
                expression{
                    BRANCH_NAME == "Div"
                }
            }
            step{
                echo "Build stage from Div Branch"
            }
        }
    }
}