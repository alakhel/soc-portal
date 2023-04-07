<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;
use App\Models\User;

class FirstTimePasswordController extends Controller
{
    public function update(Request $request)
    {
        // validate request input
        $validator = Validator::make($request->all(), [
            'username' => 'required',
            'old_password' => 'required',
            'new_password' => 'required|confirmed',
        ]);

        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        $username = $request->input('username');
        $oldPassword = $request->input('old_password');
        $newPassword = $request->input('new_password');

        // find user by username
        $user = User::where('username', $username)->first();

        if (!$user) {
            return response()->json(['error' => 'User not found'], 404);
        }

        // check if old password matches
        if (!Hash::check($oldPassword, $user->password)) {
            return response()->json(['error' => 'Incorrect password'], 401);
        }

        // update password
        $user->password = Hash::make($newPassword);
        $user->firstLogin = false;
        $user->save();

        // generate access token
        $token = $user->createToken('auth-token')->plainTextToken;

        return response()->json([
            'message' => 'Password updated successfully',
            'access_token' => $token,
            'token_type' => 'Bearer',
            'user_role' => $user->role,
        ], 200);
    }
}

