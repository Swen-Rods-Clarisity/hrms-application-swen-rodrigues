import {
    Box,
    Container,
    Typography,
} from "@mui/material";

import ForgotPasswordForm from "./ForgotPasswordForm";


function ForgotPasswordPage() {

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

                    <Box
                        sx={{
                            width: 34,
                            height: 34,

                            display: "flex",
                            alignItems: "center",
                            justifyContent: "center",

                            borderRadius: "8px",

                            backgroundColor: "#67E8F9",

                            color: "#082F36",

                            fontSize: "13px",
                            fontWeight: 700,
                        }}
                    >
                        HR
                    </Box>


                    <Typography
                        sx={{
                            color: "#FFFFFF",

                            fontSize: "18px",
                            fontWeight: 600,
                        }}
                    >
                        HRMS
                    </Typography>

                </Box>


                <ForgotPasswordForm />

            </Container>

        </Box>
    );
}


export default ForgotPasswordPage;