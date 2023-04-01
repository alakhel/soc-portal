<?php

namespace App\Http\Controllers;

use App\Models\Computer;
use Illuminate\Http\Request;
use Illuminate\Database\QueryException;
use PDOException;
use Illuminate\Support\Facades\Validator;

class ComputerController extends Controller
{
    public function index()
    {
        $computers = Computer::all();
        return response()->json($computers);
    }

    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'hostname' => 'required|unique:computers',
            'ip' => 'required|ip|unique:computers',
            'groupe' => 'required',
        ], [
            'hostname.required' => 'The hostname field is required.',
            'hostname.unique' => 'The hostname is already in use.',
            'ip.required' => 'The IP address field is required.',
            'ip.ip' => 'Please enter a valid IP address.',
            'ip.unique' => 'The IP address is already in use.',
            'groupe.required' => 'The groupe field is required.',
        ]);
    
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }
    
        try {
            $computer = Computer::create([
                'hostname' => $request->hostname,
                'ip' => $request->ip,
                'groupe' => $request->groupe,
            ]);
    
            return response()->json($computer, 201);
        } catch (QueryException $e) {
            $errorCode = $e->errorInfo[1];
            if ($errorCode == 1062) { // unique constraint violation
                return response()->json(['error' => 'Hostname or IP already exists.'], 422);
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
            $computer = Computer::findOrFail($id);
            return response()->json($computer);
        } catch (ModelNotFoundException $e) {
            return response()->json(['error' => 'Computer not found.'], 404);
        } catch (\Exception $e) {
            return response()->json(['error' => 'Database error.'], 500);
        }
    }

    public function update(Request $request, $id)
    {
        $computer = Computer::find($id);

        if (!$computer) {
            return response()->json(['error' => 'Computer not found.'], 404);
        }

        $validator = Validator::make($request->all(), [
            'hostname' => 'required|unique:computers,hostname,' . $computer->id,
            'ip' => 'required|ip|unique:computers,ip,' . $computer->id,
            'groupe' => 'required',
        ], [
            'hostname.required' => 'The hostname field is required.',
            'hostname.unique' => 'The hostname is already in use.',
            'ip.required' => 'The IP address field is required.',
            'ip.ip' => 'Please enter a valid IP address.',
            'ip.unique' => 'The IP address is already in use.',
            'groupe.required' => 'The groupe field is required.',
        ]);
        
        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }
        

        try {
            $computer->update([
                'hostname' => $request->hostname,
                'ip' => $request->ip,
                'groupe' => $request->groupe,
            ]);
            return response()->json($computer);
        } catch (\Exception $e) {
            return response()->json(['error' => 'Database error.'], 500);
        }
    }

    public function destroy($id)
    {
        try {
            $computer = Computer::findOrFail($id);
            $computer->delete();
            return response()->json(null, 204);
        } catch (ModelNotFoundException $e) {
            return response()->json(['error' => 'Computer not found.'], 404);
        } catch (\Exception $e) {
            return response()->json(['error' => 'Database error.'], 500);
        }
    }
}
