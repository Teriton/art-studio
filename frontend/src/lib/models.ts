export enum Status {
	active = 'активный',
	unactive = 'неактивный',
	canceled = 'отмененный'
	// Добавь остальные значения, если есть
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

export interface SetOfMaterialDTO {
	workhop_id: number;
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
	date: Date;
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