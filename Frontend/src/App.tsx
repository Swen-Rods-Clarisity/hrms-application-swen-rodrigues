import {
    BrowserRouter,
    Routes,
    Route,
    Navigate,
} from "react-router-dom";

import LoginPage from "./Modules/Authentication/LoginPage";
import SignupPage from "./Modules/Authentication/SignupPage";
import ForgotPasswordPage from "./Modules/Authentication/ForgotPasswordPage";



function App() {

    return (
        <BrowserRouter>

            <Routes>

                {/* Authentication */}

                <Route
                    path="/login"
                    element={<LoginPage />}
                />

                <Route
                    path="/signup"
                    element={<SignupPage />}
                />

                <Route
                    path="/forgot-password"
                    element={<ForgotPasswordPage />}
                />


                {/* Users

                <Route
                    path="/users"
                    element={<UsersPage />}
                /> */}


                {/* Default Route */}

                <Route
                    path="/"
                    element={
                        <Navigate
                            to="/login"
                            replace
                        />
                    }
                />

            </Routes>

        </BrowserRouter>
    );
}


export default App;