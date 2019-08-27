FROM openjdk:8
ADD target/docker-sprint-boot.jar docker-sprint-boot.jar
EXPOSE 8085
ENTRYPOINT ["java", "-jar", "docker-sprint-boot.jar"]