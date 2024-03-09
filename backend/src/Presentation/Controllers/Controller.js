import NewWorkWT from './WorkWT';

function NewController() {
    Controller = new Controller()
    return Controller
}
class Controller {
    constructor() {
        this._router = require('express').Router();
    }

    get router() {

        var workWT = NewWorkWT()
        this._router.use("/workWT", workWT)

        return this._router;
    }
}

