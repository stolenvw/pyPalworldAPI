responses = {
    404: {
        "description": "Item NotFound",
        "content": {
            "application/json": {
                "schema": {"type": "string", "example": {"detail": "Nothing Found"}}
            }
        },
    },
    400: {
        "description": "Missing params",
        "content": {
            "application/json": {
                "schema": {"type": "string", "example": {"detail": "Missing params"}}
            }
        },
    },
    401: {
        "description": "Unauthorized",
        "content": {
            "application/json": {
                "schema": {
                    "type": "string",
                    "example": {"detail": "string"},
                }
            }
        },
    },
}

adduser_responses = {
    409: {
        "description": "Username taken",
        "content": {
            "application/json": {
                "schema": {"type": "string", "example": {"detail": "Username is taken"}}
            }
        },
    }
}

response_401 = {
    401: {
        "description": "Unauthorized",
        "content": {
            "application/json": {
                "schema": {
                    "type": "string",
                    "example": {"detail": "string"},
                }
            }
        },
    }
}

response_401_404 = {
    404: {
        "description": "NotFound",
        "content": {
            "application/json": {
                "schema": {"type": "string", "example": {"detail": "string"}}
            }
        },
    },
    401: {
        "description": "Unauthorized",
        "content": {
            "application/json": {
                "schema": {
                    "type": "string",
                    "example": {"detail": "string"},
                }
            }
        },
    },
}

response_440_401 = {
    401: {
        "description": "Unauthorized",
        "content": {
            "application/json": {
                "schema": {
                    "type": "string",
                    "example": {"detail": "string"},
                }
            }
        },
    },
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "schema": {"type": "string", "example": {"detail": "string"}}
            }
        },
    },
}
