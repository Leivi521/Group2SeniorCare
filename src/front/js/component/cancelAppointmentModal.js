import React from "react";

export const CancelAppointmentModal = ({item, appointment, handleCancellation}) => {

    console.log(appointment.id + "appointment!!!!++")
    return (
        <div class="modal fade" id="cancelAppointmentModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="staticBackdropLabel">Confirm Cancellation</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body text-black">
                        Are you sure you want to cancel this appointment? You will not get your money back!
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        
                        {
                            item?( <button
                            onClick={() => {
                                handleCancellation(
                                    appointment.id,
                                );
                            }}
                            type="button"
                            class="btn btn-danger" data-bs-dismiss="modal">
                            Cancel Appointment
                        </button>):appointment?(
                            <button
                            onClick={() => {
                                handleCancellation(
                                    appointment.id,
                                );
                            }}
                            type="button"
                            class="btn btn-danger" data-bs-dismiss="modal">
                            Cancel Appointment
                        </button>
                        ):"Unable to cancel"
                        }
                       
                    </div>
                </div>
            </div>
        </div>
    )
}