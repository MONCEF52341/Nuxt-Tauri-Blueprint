FROM node:lts

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

RUN npm install -g pnpm

RUN pnpm install

COPY . .

RUN pnpm run webbuild

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]