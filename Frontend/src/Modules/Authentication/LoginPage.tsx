import {
    Box,
    Container,
    Typography,
} from "@mui/material";

import LoginForm from "./LoginForm";


function LoginPage() {

    return (
        <Box
            sx={{
                minHeight: "100vh",
                width: "100%",

                backgroundColor: "#0A0A0A",

                display: "flex",
                flexDirection: "column",

                alignItems: "center",
                justifyContent: "center",

                px: 2,
                py: 4,

                boxSizing: "border-box",
            }}
        >

            <Container
                maxWidth={false}
                sx={{
                    width: "100%",
                    maxWidth: "360px",

                    padding: "0 !important",
                }}
            >

                {/* HRMS Branding */}

                <Box
                    sx={{
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",

                        gap: 1,

                        marginBottom: 2.5,
                    }}
                >



                    <Typography
                        sx={{
                            color: "#FFFFFF",

                            fontSize: "18px",
                            fontWeight: 600,

                            letterSpacing: "-0.2px",
                        }}
                    >
                        Human Resource Management System
                    </Typography>

                </Box>


                <LoginForm />

            </Container>

        </Box>
    );
}


export default LoginPage;