INSERT INTO public."Basic_territory"(
	id, "registrationDate", "updateDate", name, "isActive", state_id)
	VALUES
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Carnaubais', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Chapada das Mangabeiras', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Chapada Vale do Rio Itaim', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Cocais', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Entre Rios', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Planície Litoranea', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Serra da Capivara', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Tabuleiros do Alto Parnaíba', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Vale do Canindé', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Vale do Rio Guaribas', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Vale do Sambito', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI')),
	(nextval('"Basic_territory_id_seq"'::regclass), CURRENT_DATE, CURRENT_DATE, 'Vale dos Rios Piauí e Itaueiras', True, (SELECT id FROM public."Basic_state" WHERE acronym = 'PI'));