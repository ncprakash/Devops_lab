pipeline{
    agent:any{
      enviroment  {
            IMAGE_NAME:"devops-demo-app"
            CONTAINER_NAME:"demo-container"
            APP_PORT ="5000"
        }
        stages{
            stage('build'){
               steps{     echo '📦 Stage 1: Installing dependencies...'
                bat 'pip install -r requirements.txt'
                echo '✅ Dependencies installed successfully'
               }
            }
        stage('Docker Build') {
            steps {
                echo '🐳 Stage 3: Building Docker image...'
                bat "docker build -t ${IMAGE_NAME} ."
                echo "✅ Image '${IMAGE_NAME}' built successfully"
            }
        }
        stage('Docker Deploy') {
            steps {
                echo '🚀 Stage 4: Deploying container...'

                // Stop and remove old container if running
                bat "docker stop ${CONTAINER_NAME} || exit 0"
                bat "docker rm ${CONTAINER_NAME}   || exit 0"

                // Run fresh container
                bat "docker run -d -p ${APP_PORT}:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"

                echo "✅ App deployed at http://localhost:${APP_PORT}"
            }
        }

        }
    }
      post {gi
        success {
            echo '''
            ============================================
            ✅ PIPELINE COMPLETE — ALL STAGES PASSED
            🌐 App running at http://localhost:5000
            ============================================
            '''
        }
        failure {
            echo '❌ Pipeline failed — check the stage logs above'
        }
    }
}
