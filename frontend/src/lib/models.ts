export enum Status {
	active = 'активный',
	unactive = 'неактивный',
	canceled = 'отмененный'
	// Добавь остальные значения, если есть
}

export enum PaymentStatus{
	paid = "Опалчен",
	unpaid = "Не оплачен"
}


export interface WorkshopAddDTO {
	master_id: number;
	technique_id: number;
	title: string;
	dificulty: string;
	duration: number;
	fee: number;
	status: Status;
}

export interface WorkshopDTO extends WorkshopAddDTO {
	id: number;
}

export interface WorkshopTechniqueDTO extends WorkshopDTO {
	technique: TechniqueDTO;
}

export interface WorkshopMasterDTO extends WorkshopDTO {
	master: MasterDTO;
}

export interface WorkshopRelDTO extends WorkshopDTO {
	master: MasterDTO;
	technique: TechniqueDTO;
}

export interface MasterAddDTO {
	first_name: string;
	last_name: string;
	specialization: string;
	expirience: number;
	bio: string;
}

export interface MasterDTO extends MasterAddDTO {
	id: number;
}

export interface MasterWorkshopsDTO extends MasterDTO {
	workshops: WorkshopDTO[];
}

export interface TechniqueAddDTO {
	name: string;
	discription: string;
}

export interface TechniqueDTO extends TechniqueAddDTO {
	id: number;
}

export interface TechniqueWorkshopsDTO extends TechniqueDTO {
	workshops: WorkshopDTO[];
}

export interface UserAddDTO {
	first_name: string;
	last_name: string;
	email: string;
	phone_number: string;
	login: string;
	psw: string;
	admin: boolean;
}

export interface UserDTO extends UserAddDTO {
	id: number;
}

export interface WorkshopSetsOfMaterialDTO extends WorkshopDTO {
	sets_of_materials: SetOfMaterialDTO[];
}

export interface WorkshopSessionsDTO extends WorkshopDTO {
	sessions: ScheduleDTO[];
}

export interface WorkshopAllRelDTO extends WorkshopDTO {
	master: MasterDTO;
	technique: TechniqueDTO;
	sets_of_material: SetOfMaterialDTO[];
	sessions: ScheduleDTO[];
}

export interface SetOfMaterialRawDTO {
	workshop_id: number;
	material_id: number;
	quantity: number;
	unit: string;
}

export interface SetOfMaterialDTO {
	workshop_id: number;
	material_id: number;
	quantity: number;
	unit: string;
	material: MaterialDTO;
}

export interface MaterialAddDTO {
	name: string;
	discription: string;
	cost: number;
	type: string;
}

export interface MaterialDTO extends MaterialAddDTO {
	id: number;
}

export interface MaterialRelDTO extends MaterialDTO {
	set_of_material: SetOfMaterialDTO;
}

export interface ScheduleAddDTO {
	workshop_id: number;
	date: string;
	location: string;
	numberOfSeats: number;
}

export interface ScheduleDTO extends ScheduleAddDTO {
	id: number;
}

export interface Seats {
	allSeats: number;
	occupiedSeats: number;
}

export interface ScheduleOrdersDTO extends ScheduleDTO {
  orders: OrderDTO[];
}

export interface ScheduleWorkhopDTO extends ScheduleDTO{
    workshop: WorkshopDTO
}

export interface OrderAddDTO {
  user_id: number;
  schedule_id: number;
  date: string; // ISO string
  status: Status;
}

export interface OrderDTO extends OrderAddDTO {
  id: number;
}

export interface OrderSessionDTO extends OrderDTO {
  session: ScheduleWorkhopDTO;
}

export interface OrderRelsDTO extends OrderDTO {
	session: ScheduleWorkhopDTO;
	payment: PaymentDTO;
}

export enum PaymentMethod {
  card = "карта",
  cash = "налик"
}

export interface PaymentAddDTO {
  user_id: number;
  order_id: number;
  status: PaymentStatus;
  fee: number;
  payment_method: PaymentMethod;
}

export interface PaymentDTO extends PaymentAddDTO {
  id: number;
}

export interface PaymentRelDTO extends PaymentDTO {
  user: UserDTO;
  order: OrderDTO;
}

export interface PaymentOrderDTO extends PaymentDTO {
  order: OrderSessionDTO;
}