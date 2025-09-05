pipeline {
    agent any

    options {
        // сохраняем логи поумнее и помечаем сборку как неуспешную при тест-фейлах
        timestamps()
        ansiColor('xterm')
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your/repo.git', branch: 'main' // замените на свой
            }
        }

        stage('Set up venv & install deps') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install -U pip
                    pip install -r requirements.txt
                    # полезно: ставим инструменты отчётности
                    pip install pytest pytest-html pytest-cov
                '''
            }
        }

        stage('Run pytest') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest \
                      --junitxml=report.xml \
                      --html=report.html --self-contained-html \
                      --cov=. --cov-report=xml:coverage.xml
                '''
            }
        }

        stage('Publish reports') {
            steps {
                // JUnit-отчёт -> вкладка "Test Result"
                junit allowEmptyResults: true, testResults: 'report.xml'
                // HTML-отчёт как артефакт (можно скачать/посмотреть)
                archiveArtifacts artifacts: 'report.html', fingerprint: true
                // Покрытие (если установлен плагин "Coverage" или "Cobertura")
                script {
                    // Попробуем опубликовать через Coverage plugin (если есть)
                    try {
                        publishCoverage adapters: [coberturaAdapter('coverage.xml')], sourceFileResolver: sourceFiles('STORE_ALL_BUILD')]
                    } catch (err) {
                        echo "Coverage plugin не настроен: ${err}"
                        archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
                    }
                }
            }
        }
    }

    post {
        success { echo '✅ Все тесты зелёные' }
        unstable { echo '⚠️ Есть фейлы/предупреждения' }
        failure { echo '❌ Тесты упали' }
        always  { cleanWs(deleteDirs: false, notFailBuild: true) }
    }
}
