INSERT INTO public."Basic_state"(
	id, "registrationDate", "updateDate", "codeIBGE", name, acronym, "isActive", country_id)
	VALUES 
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '21', 'Maranhão', 'MA', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '22', 'Piauí', 'PI', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '23', 'Ceará', 'CE', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '24', 'Rio Grande do Norte', 'RN', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '25', 'Paraíba', 'PB', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '26', 'Pernambuco', 'PE', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '27', 'Alagoas', 'AL', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '28', 'Sergipe', 'SE', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA')),
	(nextval('"Basic_state_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, '29', 'Bahia', 'BA', True, (SELECT id FROM public."Basic_country" WHERE acronym = 'BRA'));