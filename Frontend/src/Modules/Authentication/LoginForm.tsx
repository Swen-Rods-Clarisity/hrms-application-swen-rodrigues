import { useState } from "react";

import {
    Box,
    Button,
    Card,
    CardContent,
    TextField,
    Typography,
} from "@mui/material";

import {
    Link,
    useNavigate,
} from "react-router-dom";

import { login } from "./authService";


function LoginForm() {

    const navigate = useNavigate();


    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);


    const handleSubmit = async (
        event: React.FormEvent
    ) => {

        event.preventDefault();

        setError("");
        setLoading(true);


        try {

            const response = await login({
                username,
                password,
            });


            /*
             * Temporary storage for our
             * dummy authentication module.
             *
             * We can improve token storage
             * later.
             */

            localStorage.setItem(
                "access_token",
                response.access_token
            );


            navigate("/users");

        } catch (error) {

            if (error instanceof Error) {
                setError(error.message);
            } else {
                setError("Login failed");
            }

        } finally {

            setLoading(false);

        }
    };


    return (
        <Card
            elevation={0}
            sx={{
                width: "100%",

                backgroundColor: "#141414",

                border: "1px solid #303030",

                borderRadius: "12px",

                boxShadow:
                    "0 10px 30px rgba(0, 0, 0, 0.35)",

                color: "#FFFFFF",
            }}
        >

            <CardContent
                sx={{
                    padding: "24px",

                    "&:last-child": {
                        paddingBottom: "24px",
                    },
                }}
            >

                {/* Header */}

                <Box
                    sx={{
                        textAlign: "center",
                        marginBottom: 3,
                    }}
                >

                    <Typography
                        sx={{
                            color: "#FFFFFF",

                            fontSize: "21px",
                            lineHeight: "28px",

                            fontWeight: 600,

                            marginBottom: 0.5,
                        }}
                    >
                        Welcome back
                    </Typography>


                    <Typography
                        sx={{
                            color: "#A1A1AA",

                            fontSize: "13px",
                        }}
                    >
                        Sign in to your HRMS account
                    </Typography>

                </Box>


                {/* Error */}

                {error && (
                    <Typography
                        sx={{
                            color: "#F87171",

                            fontSize: "12px",

                            marginBottom: 2,

                            textAlign: "center",
                        }}
                    >
                        {error}
                    </Typography>
                )}


                {/* Form */}

                <Box
                    component="form"
                    onSubmit={handleSubmit}
                    sx={{
                        display: "flex",
                        flexDirection: "column",
                        gap: 2,
                    }}
                >

                    {/* Username */}

                    <Box>

                        <Typography
                            component="label"
                            htmlFor="username"
                            sx={{
                                display: "block",

                                textAlign: "left",

                                color: "#FFFFFF",

                                fontSize: "13px",
                                fontWeight: 500,

                                marginBottom: "6px",
                            }}
                        >
                            Username
                        </Typography>


                        <TextField
                            id="username"

                            fullWidth

                            value={username}

                            onChange={(event) =>
                                setUsername(
                                    event.target.value
                                )
                            }

                            placeholder="Enter your username"

                            required

                            variant="outlined"

                            slotProps={{
                                input: {
                                    sx: {
                                        height: "40px",

                                        color: "#FFFFFF",

                                        fontSize: "13px",
                                    },
                                },
                            }}

                            sx={{
                                "& .MuiOutlinedInput-root": {

                                    backgroundColor: "#1B1B1B",

                                    borderRadius: "7px",

                                    "& fieldset": {
                                        borderColor: "#303030",
                                    },

                                    "&:hover fieldset": {
                                        borderColor: "#FFFFFF",
                                    },

                                    "&.Mui-focused fieldset": {
                                        borderColor: "#FFFFFF",
                                    },
                                },

                                "& input::placeholder": {
                                    color: "#71717A",
                                    opacity: 1,
                                },
                            }}
                        />

                    </Box>


                    {/* Password */}

                    <Box>

                        <Box
                            sx={{
                                display: "flex",

                                alignItems: "center",

                                justifyContent:
                                    "space-between",

                                marginBottom: "6px",
                            }}
                        >

                            <Typography
                                component="label"
                                htmlFor="password"
                                sx={{
                                    color: "#FFFFFF",

                                    fontSize: "13px",
                                    fontWeight: 500,
                                }}
                            >
                                Password
                            </Typography>


                            <Typography
                                component={Link}
                                to="/forgot-password"
                                sx={{
                                    color: "#FFFFFF",

                                    fontSize: "12px",
                                    fontWeight: 500,

                                    textDecoration: "none",

                                    "&:hover": {
                                        color: "#FFFFFF",
                                        textDecoration:
                                            "underline",
                                    },
                                }}
                            >
                                Forgot password?
                            </Typography>

                        </Box>


                        <TextField
                            id="password"

                            fullWidth

                            type="password"

                            value={password}

                            onChange={(event) =>
                                setPassword(
                                    event.target.value
                                )
                            }

                            placeholder="Enter your password"

                            required

                            variant="outlined"

                            slotProps={{
                                input: {
                                    sx: {
                                        height: "40px",

                                        color: "#FFFFFF",

                                        fontSize: "13px",
                                    },
                                },
                            }}

                            sx={{
                                "& .MuiOutlinedInput-root": {

                                    backgroundColor: "#1B1B1B",

                                    borderRadius: "7px",

                                    "& fieldset": {
                                        borderColor: "#303030",
                                    },

                                    "&:hover fieldset": {
                                        borderColor: "#FFFFFF",
                                    },

                                    "&.Mui-focused fieldset": {
                                        borderColor: "#FFFFFF",
                                    },
                                },

                                "& input::placeholder": {
                                    color: "#71717A",
                                    opacity: 1,
                                },
                            }}
                        />

                    </Box>


                    {/* Login Button */}

                    <Button
                        type="submit"

                        fullWidth

                        variant="contained"

                        disabled={loading}

                        sx={{
                            height: "42px",

                            borderRadius: "7px",

                            backgroundColor: "#050505",

                            color: "#FFFFFF",

                            textTransform: "none",

                            fontSize: "14px",

                            fontWeight: 600,

                            boxShadow: "none",

                            marginTop: 0.5,

                            border: "1px solid #303030",

                            "&:hover": {
                                backgroundColor: "#000000",

                                boxShadow:
                                    "0 4px 14px rgba(0, 0, 0, 0.35)",
                            },

                            "&:active": {
                                backgroundColor: "#000000",
                            },
                        }}
                    >
                        {loading ? "Logging in..." : "Login"}
                    </Button>


                    {/* Signup */}

                    <Typography
                        sx={{
                            color: "#71717A",

                            fontSize: "12px",

                            textAlign: "center",

                            marginTop: 0.5,
                        }}
                    >
                        Don't have an account?{" "}

                        <Box
                            component={Link}
                            to="/signup"
                            sx={{
                                color: "#FFFFFF",

                                textDecoration: "none",

                                "&:hover": {
                                    color: "#FFFFFF",
                                    textDecoration:
                                        "underline",
                                },
                            }}
                        >
                            Sign up
                        </Box>

                    </Typography>

                </Box>

            </CardContent>

        </Card>
    );
}


export default LoginForm;