class pyPalworldAPIErrorResponses:
    response_401_409 = {
        409: {
            "description": "Conflict",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
    }

    response_401_404 = {
        404: {
            "description": "Not Found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
    }

    response_401_403_404 = {
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        404: {
            "description": "Not Found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
    }

    responses_400_401_404 = {
        404: {
            "description": "Item NotFound",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        400: {
            "description": "Missing params",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
    }

    response_400_401 = {
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
    }

    response_401_403 = {
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                        "example": {"status": 0, "message": "string"},
                    }
                }
            },
        },
    }
