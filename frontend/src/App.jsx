import React, { useState } from 'react';
import axios from 'axios';
import "./App.css";

export default function App() {
    const [skills, setSkills] = useState('');
    const [employees, setEmployees] = useState([]);
    const [hoveredEmployee, setHoveredEmployee] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');

    const handleSearch = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/search/`, {
                params: { skills }
            });

            if (response.data.message) {
                setEmployees([]);
                setErrorMessage(response.data.message);
            } else {
                setEmployees(response.data);
                setErrorMessage('');
            }
        } catch (error) {
            setErrorMessage("Error fetching data. Please try again.");
            setEmployees([]);
        }
    };

    return (
        <div className='container'>
            <h2>Employee Skill Matcher</h2>
            <input
                autoFocus
                type="text"
                placeholder="Example: CAD, MATLAB, SolidWorks"
                value={skills}
                onChange={(e) => setSkills(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>
            
            {errorMessage && <p className="error-message">{errorMessage}</p>}

            {employees.length > 0 && (
                <div>
                    <h3>Matching Employees</h3>
                    <div className="matching-container">
                        <ul>
                            {employees.map(emp => (
                                <li
                                    key={emp.id}
                                    onMouseEnter={() => setHoveredEmployee(emp)}
                                    onMouseLeave={() => setHoveredEmployee(null)}
                                >
                                    {emp.name} - {emp.skills}

                                    {hoveredEmployee && hoveredEmployee.id === emp.id && (
                                        <div className="tooltip">
                                            <p><strong>Years of Experience:</strong> {emp.years_of_experience} years</p>
                                            <p><strong>Age:</strong> {emp.age}</p>
                                            <p><strong>Location:</strong> {emp.location}</p>
                                            <p><strong>Current Task:</strong> {emp.present_tasks}</p>
                                            <p><strong>Current Project:</strong> {emp.present_project}</p>
                                            <p><strong>Nearest Deadline:</strong> {emp.nearest_deadline}</p>
                                        </div>
                                    )}
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
            )}
        </div>
    );
}
