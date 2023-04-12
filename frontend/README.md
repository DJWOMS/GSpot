# GSpot Frontend

[Next.js Documentation](https://nextjs.org/docs/getting-started).  
[Next.js Beta Documentation](https://beta.nextjs.org/docs/getting-started).  

Some functionality of Next 13.2+ is unstable.

## Folder Structure
### app
The app folder contains routing configuration for the entire service.

File Convention:

- layout.js  
A custom user interface used across routes.

- page.js  
A unique user interface for the route.

- loading.js  
Loading state while page content is still being loaded.

- error.js  
Message displayed to the user when an error occurs.

- not-found.js  
The not-found file is used to render UI when the notFound function is thrown within a route segment.

- route.js  
A custom request handler for this route, similar to an API endpoint call.

### components
The components folder contains all React components that are used globally.

### features
The features folder contains modules related to specific functionality.

### lib
The lib folder contains libraries or packages used in the application.

### public
The public folder contains media files that may be required for display on the website.

### utils 
The utils folder contains various utilities and functions used in the application. Each file contains only one function, and the file name is determined by the function name.


## Installation and Setup
Before starting work, you need to install all the necessary files required to work with the project. Run `npm i` or `npm install`.

Running this command will also add a git hook to automatically format code (see [Husky](https://typicode.github.io/husky/#/)). In the future, each local commit will automatically format all files with the extensions `.js`, `.jsx`, `.ts`, `.tsx`. To change this behavior, use the `.lintstagedrc`, `.husky/pre-commit` files in the project root.

### Local Development
#### Using Docker
To run the project in dev mode, docker-compose is used. To start the project, run:

```
docker-compose up
```
This command will create a Docker container and run a web server inside it. Docker Compose in this case allows you to automatically restart the web server when the project source code files are changed.   

#### Without Docker
```
npm run dev
```  
Starts the application in development mode on port `3000`.

```
npm run build
```  
Builds the application for production mode.

```
npm start
```  
Starts the application in production mode.

### Mocks Server
We are using the server's built-in next.js functions. More details can be found in the [`CONTRIBUTING.md`](repo/blob/master/CONTRIBUTING.md) file.


### Server Deployment
Compile the files into a single container for further deployment. Use the `make build` command or:
```
docker build -f Dockerfile.prod -t gspot-frontend:latest .
```

To start the compiled container, use the `make run` command or:

```
docker run --name gspot_production_frontend -d -p 3000:3000 gspot-frontend:latest
```

## Contributing
Fork this repository to your account. After making the necessary changes, create a pull request.  
More details are described in a special file [`CONTRIBUTING.md`](repo/blob/master/CONTRIBUTING.md).


## Github Actions
- Retrieve your Vercel [Access Token](https://vercel.com/guides/how-do-i-use-a-vercel-api-access-token);
- Install the [Vercel CLI](https://vercel.com/docs/cli) and run `vercel login`;
- Inside `frontend` folder, run `vercel link` to create a new Vercel project;
- Inside the generated `frontend/.vercel` folder, save the `projectId` and `orgId` from the `project.json`;
- Inside GitHub, add `VERCEL_TOKEN`, `VERCEL_ORG_ID`, and `VERCEL_PROJECT_ID` as secrets.
