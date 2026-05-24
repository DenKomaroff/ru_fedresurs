from ..api import BaseAPI
import xmltodict


class MessagesAPI(BaseAPI):

    def __init__(self, url):
        super().__init__(url)
        self.url = f'{url}/v1/messages'

    def execute(self, ses, **kwargs):
        self._prepare_params(**kwargs)
        response = ses.request(method='get', url=self.url, params=self.params, verify=False)
        result = response.json() if response.status_code == 200 else response
        return result

    def by_id(self, ses, guid):
        response = ses.request(method='get', url=f'{self.url}/{guid}', verify=False)
        result = response.json() if response.status_code == 200 else response
        return result

    def files(self, ses, guid):
        response = ses.request(method='get', url=f'{self.url}/{guid}/files/archive', verify=False)
        result = response.content if response.status_code == 200 else response
        return result

    def linked(self, ses, guid):
        response = ses.request(method='get', url=f'{self.url}/{guid}/linked', verify=False)
        result = response.json() if response.status_code == 200 else response
        return result


class Message:

    def __init__(self, data=None):
        self.data = data
        self.guid = None
        self.bankrupt_guid = None
        self.number = None
        self.date_publish = None
        self.content = None
        # self.content1 = None
        self.type = None

        self.init_data()
        self._parse_content()

    def init_data(self):
        if self.data is not None:
            self.guid = self.data.get('guid')
            self.bankrupt_guid = self.data.get('bankruptGuid')
            self.number = self.data.get('number')
            self.date_publish = self.data.get('datePublish')
            # self.content = self.data.get('content')
            self.content = xmltodict.parse(self.data.get('content'))
            self.type = self.data.get('type')
            match self.type:
                case 'ArbitralDecree': self.__class__ = Message
                case 'ExtraordinaryExpenses': self.__class__ = Message
                case 'ApplicationReviewCourtDecision': self.__class__ = Message
                case 'Other': self.__class__ = Message
                case 'Annul': self.__class__ = Message
                case 'ReceivingCreditorDemand': self.__class__ = Message
                case 'ReceivingCreditorDemand2': self.__class__ = Message
                case 'CreditorsDemandRegistered': self.__class__ = Message
                case 'IntentionOfDemandsFulfilment': self.__class__ = Message
                case 'IntentionOfDemandsFulfilmentReview': self.__class__ = Message
                case 'FulfilledDemandsRecognition': self.__class__ = Message
                case 'FulfilledDemandsRecognitionReview': self.__class__ = Message
                case 'CourtAssertAcceptance': self.__class__ = Message
                case 'Rebuttal': self.__class__ = Message
                case 'DisqualificationArbitrationManager': self.__class__ = Message
                case 'DisqualificationArbitrationManager2': self.__class__ = Message
                case 'Meeting': self.__class__ = Message
                case 'Meeting2': self.__class__ = Message
                case 'MeetingResult': self.__class__ = Message
                case 'Committee': self.__class__ = Message
                case 'Committee2': self.__class__ = Message
                case 'CommitteeResult': self.__class__ = Message
                case 'CourtAcceptanceStatement': self.__class__ = Message
                case 'MeetingParticipantsBuilding': self.__class__ = Message
                case 'MeetingParticipantsBuilding2': self.__class__ = Message
                case 'MeetingPartBuildResult': self.__class__ = Message
                case 'PartBuildMonetaryClaim': self.__class__ = Message
                case 'TransferOwnershipRealEstate': self.__class__ = Message
                case 'FinancialStateInformation': self.__class__ = Message
                case 'AssetsReturning': self.__class__ = Message
                case 'PropertyInventoryResult': self.__class__ = Message
                case 'PropertyEvaluationReport': self.__class__ = Message
                case 'AssessmentReport': self.__class__ = Message
                case 'TransferInsurancePortfolio': self.__class__ = Message
                case 'BankOpenAccountDebtor': self.__class__ = Message
                case 'CourseOfSalePersonProperty': self.__class__ = Message
                case 'Auction': self.__class__ = Message
                case 'Auction2': self.__class__ = Message
                case 'TradeResult': self.__class__ = Message
                case 'SaleContractResult': self.__class__ = Message
                case 'SaleOrderPledgedProperty': self.__class__ = Message
                case 'SaleOrderPledgedProperty2': self.__class__ = Message
                case 'CancelAuctionTradeResult': self.__class__ = Message
                case 'ChangeAuction': self.__class__ = Message
                case 'ChangeAuction2': self.__class__ = Message
                case 'SaleContractResult2': self.__class__ = Message
                case 'RightUnsoldAsset': self.__class__ = Message
                case 'ChangeSaleContractResult': self.__class__ = Message
                case 'ProcedureGrantingIndemnity': self.__class__ = Message
                case 'MortgageSaleExclusion': self.__class__ = Message
                case 'MeetingWorker': self.__class__ = Message
                case 'MeetingWorker2': self.__class__ = Message
                case 'MeetingWorkerResult': self.__class__ = Message
                case 'DealInvalid': self.__class__ = Message
                case 'DealInvalid2': self.__class__ = Message
                case 'ActDealInvalid': self.__class__ = Message
                case 'ActDealInvalid2': self.__class__ = Message
                case 'ActReviewDealInvalid2': self.__class__ = Message
                case 'ActReviewDealInvalid': self.__class__ = Message
                case 'DealInvalidResult': self.__class__ = Message
                case 'DealInvalidResult2': self.__class__ = Message
                case 'DeclarationPersonDamages': self.__class__ = Message
                case 'ActPersonDamages': self.__class__ = Message
                case 'PersonResponsibilityDeclaration': self.__class__ = Message
                case 'ActReviewPersonDamages': self.__class__ = Message
                case 'DeclarationPersonSubsidiary': self.__class__ = Message
                case 'PersonResponsibilityResult': self.__class__ = Message
                case 'ActPersonSubsidiary': self.__class__ = Message
                case 'ActPersonSubsidiary2': self.__class__ = Message
                case 'ActReviewPersonSubsidiary2': self.__class__ = Message
                case 'ActReviewPersonSubsidiary': self.__class__ = Message
                case 'CreditorChoiceRightSubsidiary': self.__class__ = Message
                case 'AccessionDeclarationSubsidiary': self.__class__ = Message
                case 'ChangeCreditorChoiceRightSubsidiary': self.__class__ = Message
                case 'RightOfAcquisitionExecution': self.__class__ = Message
                case 'AppointAdministration': self.__class__ = Message
                case 'ChangeAdministration': self.__class__ = Message
                case 'TerminationAdministration': self.__class__ = Message
                case 'DemandAnnouncement': self.__class__ = Message
                case 'BankPayment': self.__class__ = Message
                case 'IntentionCreditOrg': self.__class__ = Message
                case 'LiabilitiesCreditOrg': self.__class__ = Message
                case 'PerformanceCreditOrg': self.__class__ = Message
                case 'BuyingProperty': self.__class__ = Message
                case 'ReducingSizeShareCapital': self.__class__ = Message
                case 'SelectionPurchaserAssets': self.__class__ = Message
                case 'ImpendingTransferAssets': self.__class__ = Message
                case 'TransferAssets': self.__class__ = Message
                case 'EstimatesCurrentExpenses': self.__class__ = Message
                case 'OrderAndTimingCalculations': self.__class__ = Message
                case 'ChangeEstimatesCurrentExpenses': self.__class__ = Message
                case 'InformationAboutBankruptcy': self.__class__ = Message
                case 'EstimatesAndUnsoldAssets': self.__class__ = Message
                case 'RemainingAssetsAndRight': self.__class__ = Message
                case 'ExtensionAdministration': self.__class__ = Message
                case 'TransferResponsibilitiesFund': self.__class__ = Message
                case 'StartSettlement': self.__class__ = Message
                case 'ProcessInventoryDebtor': self.__class__ = Message
                case 'RefusalOfIntentionCreditOrg': self.__class__ = Message
                case 'LiabilitiesCreditOrgAct': self.__class__ = Message
                case 'BeginExecutoryProcess': self.__class__ = Message
                case 'TransferAssertsForImplementation': self.__class__ = Message
                case 'ViewDraftRestructuringPlan': self.__class__ = Message
                case 'ViewExecRestructuringPlan': self.__class__ = Message
                case 'DeliberateBankruptcy': self.__class__ = Message
                case 'CancelDeliberateBankruptcy': self.__class__ = Message
                case 'ChangeDeliberateBankruptcy': self.__class__ = Message
                case 'StartOfExtrajudicialBankruptcy': self.__class__ = Message
                case 'ReturnOfApplicationOnExtrajudicialBankruptcy': self.__class__ = Message
                case 'TerminationOfExtrajudicialBankruptcy': self.__class__ = Message

    def _parse_content(self):
        self.bankruptcy_case_number = self.content.get('MessageData').get('CaseNumber')
        self.publisher = self.content.get('MessageData').get('Publisher')
        self.message_info = self.content.get('MessageData').get('MessageInfo')
        self.text = self.message_info.get(self.type).get('Text')

        # MessageInfo
        # Bankrupt
