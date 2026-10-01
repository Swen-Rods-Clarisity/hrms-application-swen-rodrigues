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

import { resetPassword } from "./authService";


function ForgotPasswordForm() {

    const navigate = useNavigate();


    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] =
        useState("");

    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);


    const handleSubmit = async (
        event: React.FormEvent
    ) => {

        event.preventDefault();

        setError("");


        if (password !== confirmPassword) {

            setError(
                "Passwords do not match"
            );

            return;
        }


        setLoading(true);


        try {

            await resetPassword({
                username,
                new_password: password,
            });


            navigate("/login");

        } catch (error) {

            if (error instanceof Error) {
                setError(error.message);
            } else {
                setError(
                    "Password reset failed"
                );
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
                            fontWeight: 600,

                            marginBottom: 0.5,
                        }}
                    >
                        Reset password
                    </Typography>


                    <Typography
                        sx={{
                            color: "#A1A1AA",

                            fontSize: "13px",
                        }}
                    >
                        Create a new password
                    </Typography>

                </Box>


                {error && (
                    <Typography
                        sx={{
                            color: "#F87171",

                            fontSize: "12px",

                            textAlign: "center",

                            marginBottom: 2,
                        }}
                    >
                        {error}
                    </Typography>
                )}


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

                                color: "#A5F3FC",

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
                                        borderColor: "#67E8F9",
                                    },

                                    "&.Mui-focused fieldset": {
                                        borderColor: "#67E8F9",
                                    },
                                },

                                "& input::placeholder": {
                                    color: "#71717A",
                                    opacity: 1,
                                },
                            }}
                        />

                    </Box>


                    {/* New Password */}

                    <Box>

                        <Typography
                            component="label"
                            htmlFor="password"
                            sx={{
                                display: "block",

                                color: "#A5F3FC",

                                fontSize: "13px",
                                fontWeight: 500,

                                marginBottom: "6px",
                            }}
                        >
                            New Password
                        </Typography>


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

                            placeholder="Enter new password"

                            required

                            variant="outlined"

                            slotProps={{
                                input: {
                                    sx: {
                                        height: "40px",
                                        color: "#FFFFFF",
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
                                        borderColor: "#67E8F9",
                                    },

                                    "&.Mui-focused fieldset": {
                                        borderColor: "#67E8F9",
                                    },
                                },

                                "& input::placeholder": {
                                    color: "#71717A",
                                    opacity: 1,
                                },
                            }}
                        />

                    </Box>


                    {/* Confirm Password */}

                    <Box>

                        <Typography
                            component="label"
                            htmlFor="confirm-password"
                            sx={{
                                display: "block",

                                color: "#A5F3FC",

                                fontSize: "13px",
                                fontWeight: 500,

                                marginBottom: "6px",
                            }}
                        >
                            Confirm New Password
                        </Typography>


                        <TextField
                            id="confirm-password"

                            fullWidth

                            type="password"

                            value={confirmPassword}

                            onChange={(event) =>
                                setConfirmPassword(
                                    event.target.value
                                )
                            }

                            placeholder="Confirm new password"

                            required

                            variant="outlined"

                            slotProps={{
                                input: {
                                    sx: {
                                        height: "40px",
                                        color: "#FFFFFF",
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
                                        borderColor: "#67E8F9",
                                    },

                                    "&.Mui-focused fieldset": {
                                        borderColor: "#67E8F9",
                                    },
                                },

                                "& input::placeholder": {
                                    color: "#71717A",
                                    opacity: 1,
                                },
                            }}
                        />

                    </Box>


                    {/* Reset Button */}

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

                            border: "1px solid #303030",

                            "&:hover": {
                                backgroundColor: "#000000",
                            },
                        }}
                    >
                        {loading
                            ? "Resetting..."
                            : "Reset Password"}
                    </Button>


                    {/* Back To Login */}

                    <Typography
                        sx={{
                            color: "#71717A",

                            fontSize: "12px",

                            textAlign: "center",
                        }}
                    >
                        Remember your password?{" "}

                        <Box
                            component={Link}
                            to="/login"
                            sx={{
                                color: "#A5F3FC",

                                textDecoration: "none",

                                "&:hover": {
                                    color: "#67E8F9",
                                    textDecoration:
                                        "underline",
                                },
                            }}
                        >
                            Login
                        </Box>

                    </Typography>

                </Box>

            </CardContent>

        </Card>
    );
}


export default ForgotPasswordForm;