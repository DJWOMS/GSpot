FROM node:19-alpine 

RUN npm install -g localtunnel
COPY ./tunnel/tunnel.sh /tunnel/tunnel.sh

ENTRYPOINT ["sh", "/tunnel/tunnel.sh"]