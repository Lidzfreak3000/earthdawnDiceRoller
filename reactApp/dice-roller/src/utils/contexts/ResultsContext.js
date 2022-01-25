import React from "react";

export const ResultsContext = React.createContext({
     value: null, 
     setValue: () => {}, 
     stepsValue: null, 
     setStepsValue: () => {} 
    });