import { JsonDecoder } from "ts.data.json";

export class VariableObject {
  isSecret?: boolean;
  value: string = "";
}

export interface Value {
  variables: { [variableName: string]: VariableObject };
  id: number;
  type: string;
  name: string;
  createdBy: EdBy;
  createdOn: Date;
  modifiedBy: EdBy;
  modifiedOn: Date;
  isShared: boolean;
}

export interface EdBy {
  displayName: string;
  id: string;
  uniqueName: string;
}

export interface RootObject {
  count: number;
  value: Value[];
}

var originalJson: RootObject = JSON.parse(
  '{"count":1,"value":[{"variables":{"123456798":{"value":"passed"},"foo":{"value":"bar"}},"id":1,"type":"Vsts","name":"SonarCloud","createdBy":{"displayName":"Project Collection Build Service (mickaelcarosonar)","id":"f5166eff-92bc-4acb-a62b-2325d3030ae3","uniqueName":"Build\d6d75013-478c-4386-8814-90a393c07f5e"},"createdOn":"2019-07-09T12:46:00.1633333Z","modifiedBy":{"displayName":"Mickaël Caro","id":"986b3b0a-6ea9-6ccc-952b-eeb5ddce40d6","uniqueName":"mickael.caro@sonarsource.com"},"modifiedOn":"2019-07-09T14:35:34.3633333Z","isShared":false}]}'
);

console.debug(JSON.stringify(originalJson.value[0].variables["123456798"]));

let ceTaskId = "newtaskid";
let qualityGateStatus = "failed";

originalJson.value[0].variables[ceTaskId] = new VariableObject(); 
originalJson.value[0].variables[ceTaskId].value = qualityGateStatus;

console.debug(JSON.stringify(originalJson.value[0].variables[ceTaskId]));

let newVariables = JSON.stringify(originalJson.value[0].variables);

console.debug(newVariables);
