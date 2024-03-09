
function NewWorkWT() {
    usecase = require('../../Application/UseCases/WorkWT')
    WorkWT = new WorkWT(usecase)
    return WorkWT
}
class WorkWT {
  constructor(usecase) {
    this.usecase= usecase;
  }
    TextToS(){}
    TextToSy(){}
    SymbolsToT(){}
    SpeechToT(){}
}

exports.default = WorkWT;