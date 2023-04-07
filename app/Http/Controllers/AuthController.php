<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;

class AuthController extends Controller
{
    public function login(Request $request)
    {
        // validate user credentials
        $validator = Validator::make($request->all(), [
            'username' => 'required',
            'password' => 'required',
        ]);

        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        // attempt to authenticate user
        if (Auth::attempt($validator->validated())) {
            // get the authenticated user
            $user = Auth::user();

            // if first login, return a message to the frontend
            if ($user->firstLogin) {
                return response()->json([
                    'message' => 'Please change your password.',
                ], 200);
            }

            // authentication successful, generate token
            $token = $user->createToken('auth-token')->plainTextToken;

            return response()->json([
                'access_token' => $token,
                'token_type' => 'Bearer',
                'user_role' => $user->role, // Add this line

            ]);
        }

        // authentication failed, return error response
        return response()->json([
            'error' => 'Incorrect password',
        ], 401);
    }
}
