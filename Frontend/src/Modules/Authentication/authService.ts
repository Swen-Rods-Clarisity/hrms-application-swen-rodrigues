const API_URL =
    "http://127.0.0.1:8000/api/v1/auth";


export interface LoginRequest {
    username: string;
    password: string;
}


export interface SignupRequest {
    username: string;
    password: string;
}


export interface ResetPasswordRequest {
    username: string;
    new_password: string;
}


export interface LoginResponse {
    access_token: string;
    token_type: string;
}


export interface UserResponse {
    id: number;
    username: string;
    created_at: string;
}


/* ---------------- LOGIN ---------------- */

export async function login(
    data: LoginRequest
): Promise<LoginResponse> {

    const response = await fetch(
        `${API_URL}/login`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(data),
        }
    );


    if (!response.ok) {

        const errorData = await response.json();

        throw new Error(
            errorData.detail ||
            "Login failed"
        );
    }


    return response.json();
}


/* ---------------- SIGNUP ---------------- */

export async function signup(
    data: SignupRequest
): Promise<UserResponse> {

    const response = await fetch(
        `${API_URL}/signup`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(data),
        }
    );


    if (!response.ok) {

        const errorData = await response.json();

        throw new Error(
            errorData.detail ||
            "Signup failed"
        );
    }


    return response.json();
}


/* ---------------- RESET PASSWORD ---------------- */

export async function resetPassword(
    data: ResetPasswordRequest
): Promise<UserResponse> {

    const response = await fetch(
        `${API_URL}/reset-password`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(data),
        }
    );


    if (!response.ok) {

        const errorData = await response.json();

        throw new Error(
            errorData.detail ||
            "Password reset failed"
        );
    }


    return response.json();
}


/* ---------------- CURRENT USER ---------------- */

export async function getCurrentUser(
    token: string
): Promise<UserResponse> {

    const response = await fetch(
        `${API_URL}/me`,
        {
            method: "GET",

            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );


    if (!response.ok) {

        const errorData = await response.json();

        throw new Error(
            errorData.detail ||
            "Unable to get current user"
        );
    }


    return response.json();
}