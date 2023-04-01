<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\ValidationException;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Facades\Auth;


class UserController extends Controller
{
    public function index()
    {
        $users = User::all();
        return response()->json($users);
    }

    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'prenom' => 'required',
            'nom' => 'required',
            'username' => 'required|unique:users',
            'password' => 'required',
            'firstLogin' => 'boolean',
            'groupe' => 'required',
        ]);

        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        try {
            $user = User::create(array_merge($request->all(), [
                'password' => Hash::make($request->input('password'))
            ]));
            return response()->json($user, 201);
        } catch (QueryException $e) {
            $errorCode = $e->errorInfo[1];
            if ($errorCode == 1062) { // unique constraint violation
                return response()->json(['error' => 'Username already exists.'], 422);
            } else {
                // handle other database exceptions as necessary
                if ($e->getPrevious() instanceof PDOException) {
                    // handle PDOException
                    return response()->json(['error' => 'Database error.'], 500);
                } else {
                    // re-throw the exception for other types of QueryException
                    throw $e;
                }
            }
        }
    }
    public function authenticatedUser()
    {
        $user = Auth::user();
        return response()->json($user, 200);
    }
    public function update(Request $request, $id)
    {
        $validator = Validator::make($request->all(), [
            'prenom' => 'sometimes|required',
            'nom' => 'sometimes|required',
            'username' => 'sometimes|required|unique:users,username,'.$id,
            'password' => 'sometimes|required',
            'firstLogin' => 'boolean',
            'groupe' => 'sometimes|required',
        ]);

        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        try {
            $user = User::findOrFail($id);
            $user->update(array_merge($request->all(), [
                'password' => Hash::make($request->input('password'))
            ]));
            return response()->json($user, 200);
        } catch (ModelNotFoundException $e) {
            return response()->json(['error' => 'User not found.'], 404);
        } catch (QueryException $e) {
            $errorCode = $e->errorInfo[1];
            if ($errorCode == 1062) { // unique constraint violation
                return response()->json(['error' => 'Username already exists.'], 422);
            } else {
                // handle other database exceptions as necessary
                if ($e->getPrevious() instanceof PDOException) {
                    // handle PDOException
                    return response()->json(['error' => 'Database error.'], 500);
                } else {
                    // re-throw the exception for other types of QueryException
                    throw $e;
                }
            }
        }
    }

    public function show($id)
    {
        try {
            $user = User::findOrFail($id);
            return response()->json($user, 200);
        } catch (ModelNotFoundException $e) {
            return response()->json(['error' => 'User not found.'], 404);
        }
    }

    public function destroy($id)
    {
        try {
            $user = User::findOrFail($id);
            $user->delete();
            return response()->json(null, 204);
        } catch (ModelNotFoundException $e) {
            return response()->json(['error' => 'User not found.'], 404);
        } catch (QueryException $e) {
            // handle other database exceptions as necessary
            if ($e->getPrevious() instanceof PDOException) {
                // handle PDOException
                return response()->json(['error' => 'Database error.'], 500);
            } else {
                // re-throw the exception for other types of QueryException
                throw $e;
            }
        }
    }
}
