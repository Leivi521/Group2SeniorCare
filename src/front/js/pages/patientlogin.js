import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/patientlogin.css";

const PatientLogin = () => {
    const { store, actions } = useContext(Context);

    return (
        <div className="container-patientlogin">
            <div className="row justify-content-center">
                <div className="col-md-12"> 
                    <h1 className="text-center">Patient Log-in</h1>
                    <form onSubmit={(e) => {
                        e.preventDefault();
                        actions.loginPatient(e.target.email.value, e.target.password.value);
                    }}>
                        <div className="form-group">
                            <label htmlFor="email">Email address</label>
                            <input type="email" className="form-control" id="email" name="email" placeholder="Enter email" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Password</label>
                            <div className="input-group mb-3">
                                <input type="password" className="form-control" id="password" name="password" placeholder="Password" />
                                <div className="input-group-append">
                                    <span className="input-group-text">
                                        <i className="far fa-eye"></i>
                                    </span>
                                </div>
                            </div>
                        </div>
                        <button type="submit" className="btn btn-primary w-100">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default PatientLogin;