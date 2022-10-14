## Available Scripts

## Frontend

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

## Backend
### `yarn start-api`
Starts Api

Please add virtual environment inside backend folder by running following commands
```
python3 -m venv venv
source venv/bin/activate
```
The project needs api key. You can set API key on the environment as `API_KEY=1234` or add `.env` file with the same value.

### Tentative Architecture
![Alt text](/weatherapp.jpg?raw=true "Architecture")

### Run python tests
run `pytest` inside backend folder

Datalayer test is skipped because it makes actual request to API and we only have 500 calls for free tier. To run it unskip that test.

More tests can be added, I have added few key tests to validate things are working fine. The framework is there to test out multiple other edge cases

### Why use Protocol and Typings?

1. To ensure discussion about the interface.
2. Run `mypy` and catch type errors beforehand

Application should look like the following after it runs. It builds on the existing react app styles

![Alt text](/weather_app.gif?raw=true "Application")


