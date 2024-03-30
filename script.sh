# Construction de l'image Docker
docker build -t image_ulrich .

# Connexion à Docker (assurez-vous que Docker Desktop est en cours d'exécution sur votre machine)
docker login

# Téléchargement de l'image Docker (si elle n'est pas déjà téléchargée localement)
docker pull nom_image

# Tag de l'image pour la publication sur Docker Hub
docker tag image_ulrich nom_utilisateur_dockerhub/nom_image:v1

# Publication de l'image sur Docker Hub
docker push nom_utilisateur_dockerhub/nom_image:v1
