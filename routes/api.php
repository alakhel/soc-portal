<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;
use App\Http\Controllers\ComputerController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\FirstTimePasswordController;

Route::get('/example', function (Request $request) {
    return response()->json(['message' => 'Hello, API!']);
});

Route::apiResource('users', UserController::class);
Route::apiResource('computers', ComputerController::class);
Route::post('/login', [AuthController::class, 'login']);
Route::post('/first-time-password', [FirstTimePasswordController::class, 'update']);

Route::middleware('auth:api')->group(function () {
    Route::get('/user', [UserController::class, 'authenticatedUser']);
    // Other protected routes can be added here
});