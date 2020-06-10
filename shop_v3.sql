PGDMP                 
        x            shop_v3    12.0    12.0 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    34080    shop_v3    DATABASE     �   CREATE DATABASE shop_v3 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE shop_v3;
                postgres    false            �            1259    34147 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    34145    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    213            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    212            �            1259    34157    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    34155    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    215            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    214            �            1259    34139    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    34137    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    211            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    210            �            1259    34357 	   cart_cart    TABLE     v   CREATE TABLE public.cart_cart (
    id integer NOT NULL,
    active boolean NOT NULL,
    user_id integer NOT NULL
);
    DROP TABLE public.cart_cart;
       public         heap    postgres    false            �            1259    34355    cart_cart_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.cart_cart_id_seq;
       public          postgres    false    226            �           0    0    cart_cart_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.cart_cart_id_seq OWNED BY public.cart_cart.id;
          public          postgres    false    225            �            1259    34376    cart_cartitem    TABLE     �   CREATE TABLE public.cart_cartitem (
    id integer NOT NULL,
    quantity integer NOT NULL,
    cart_id integer NOT NULL,
    product_id integer NOT NULL
);
 !   DROP TABLE public.cart_cartitem;
       public         heap    postgres    false            �            1259    34374    cart_cartitem_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_cartitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.cart_cartitem_id_seq;
       public          postgres    false    230            �           0    0    cart_cartitem_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.cart_cartitem_id_seq OWNED BY public.cart_cartitem.id;
          public          postgres    false    229            �            1259    34365 
   cart_order    TABLE     !  CREATE TABLE public.cart_order (
    id integer NOT NULL,
    amount double precision NOT NULL,
    order_time timestamp with time zone NOT NULL,
    payment_method character varying(4) NOT NULL,
    address character varying(250) NOT NULL,
    notes text,
    cart_id integer NOT NULL
);
    DROP TABLE public.cart_order;
       public         heap    postgres    false            �            1259    34363    cart_order_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.cart_order_id_seq;
       public          postgres    false    228            �           0    0    cart_order_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.cart_order_id_seq OWNED BY public.cart_order.id;
          public          postgres    false    227            �            1259    34115    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    34113    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    209            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    208            �            1259    34105    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    34103    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    207            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    206            �            1259    34083    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    34081    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    203            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    202            �            1259    34189    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �            1259    34226    shop_category    TABLE     h   CREATE TABLE public.shop_category (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);
 !   DROP TABLE public.shop_category;
       public         heap    postgres    false            �            1259    34224    shop_category_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shop_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.shop_category_id_seq;
       public          postgres    false    220            �           0    0    shop_category_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.shop_category_id_seq OWNED BY public.shop_category.id;
          public          postgres    false    219            �            1259    34201    shop_product    TABLE     !  CREATE TABLE public.shop_product (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    category_id integer NOT NULL,
    color character varying(50) NOT NULL,
    cost double precision NOT NULL,
    description text NOT NULL,
    image character varying(100) NOT NULL
);
     DROP TABLE public.shop_product;
       public         heap    postgres    false            �            1259    34199    shop_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shop_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.shop_product_id_seq;
       public          postgres    false    218            �           0    0    shop_product_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.shop_product_id_seq OWNED BY public.shop_product.id;
          public          postgres    false    217            �            1259    34247    users_loyaltycard    TABLE     �   CREATE TABLE public.users_loyaltycard (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    discount double precision NOT NULL
);
 %   DROP TABLE public.users_loyaltycard;
       public         heap    postgres    false            �            1259    34245    users_loyaltycard_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_loyaltycard_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.users_loyaltycard_id_seq;
       public          postgres    false    222            �           0    0    users_loyaltycard_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.users_loyaltycard_id_seq OWNED BY public.users_loyaltycard.id;
          public          postgres    false    221            �            1259    34094    users_myuser    TABLE     �   CREATE TABLE public.users_myuser (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    email character varying(255) NOT NULL,
    is_active boolean NOT NULL,
    is_admin boolean NOT NULL
);
     DROP TABLE public.users_myuser;
       public         heap    postgres    false            �            1259    34092    users_myuser_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_myuser_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.users_myuser_id_seq;
       public          postgres    false    205            �           0    0    users_myuser_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.users_myuser_id_seq OWNED BY public.users_myuser.id;
          public          postgres    false    204            �            1259    34256    users_profile    TABLE     �   CREATE TABLE public.users_profile (
    id integer NOT NULL,
    name character varying(50),
    loyalty_card_id integer,
    user_id integer NOT NULL
);
 !   DROP TABLE public.users_profile;
       public         heap    postgres    false            �            1259    34254    users_profile_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.users_profile_id_seq;
       public          postgres    false    224            �           0    0    users_profile_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.users_profile_id_seq OWNED BY public.users_profile.id;
          public          postgres    false    223            �
           2604    34150    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    213    212    213            �
           2604    34160    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �
           2604    34142    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    211    210    211            �
           2604    34360    cart_cart id    DEFAULT     l   ALTER TABLE ONLY public.cart_cart ALTER COLUMN id SET DEFAULT nextval('public.cart_cart_id_seq'::regclass);
 ;   ALTER TABLE public.cart_cart ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            �
           2604    34379    cart_cartitem id    DEFAULT     t   ALTER TABLE ONLY public.cart_cartitem ALTER COLUMN id SET DEFAULT nextval('public.cart_cartitem_id_seq'::regclass);
 ?   ALTER TABLE public.cart_cartitem ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    230    230            �
           2604    34368    cart_order id    DEFAULT     n   ALTER TABLE ONLY public.cart_order ALTER COLUMN id SET DEFAULT nextval('public.cart_order_id_seq'::regclass);
 <   ALTER TABLE public.cart_order ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    227    228    228            �
           2604    34118    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    208    209    209            �
           2604    34108    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    207    206    207            �
           2604    34086    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �
           2604    34229    shop_category id    DEFAULT     t   ALTER TABLE ONLY public.shop_category ALTER COLUMN id SET DEFAULT nextval('public.shop_category_id_seq'::regclass);
 ?   ALTER TABLE public.shop_category ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            �
           2604    34204    shop_product id    DEFAULT     r   ALTER TABLE ONLY public.shop_product ALTER COLUMN id SET DEFAULT nextval('public.shop_product_id_seq'::regclass);
 >   ALTER TABLE public.shop_product ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �
           2604    34250    users_loyaltycard id    DEFAULT     |   ALTER TABLE ONLY public.users_loyaltycard ALTER COLUMN id SET DEFAULT nextval('public.users_loyaltycard_id_seq'::regclass);
 C   ALTER TABLE public.users_loyaltycard ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222            �
           2604    34097    users_myuser id    DEFAULT     r   ALTER TABLE ONLY public.users_myuser ALTER COLUMN id SET DEFAULT nextval('public.users_myuser_id_seq'::regclass);
 >   ALTER TABLE public.users_myuser ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            �
           2604    34259    users_profile id    DEFAULT     t   ALTER TABLE ONLY public.users_profile ALTER COLUMN id SET DEFAULT nextval('public.users_profile_id_seq'::regclass);
 ?   ALTER TABLE public.users_profile ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224            �          0    34147 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    213   �       �          0    34157    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    215   �       �          0    34139    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    211   ,�       �          0    34357 	   cart_cart 
   TABLE DATA           8   COPY public.cart_cart (id, active, user_id) FROM stdin;
    public          postgres    false    226   C�       �          0    34376    cart_cartitem 
   TABLE DATA           J   COPY public.cart_cartitem (id, quantity, cart_id, product_id) FROM stdin;
    public          postgres    false    230   ��       �          0    34365 
   cart_order 
   TABLE DATA           e   COPY public.cart_order (id, amount, order_time, payment_method, address, notes, cart_id) FROM stdin;
    public          postgres    false    228   g�       �          0    34115    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    209   г       �          0    34105    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    207   ��       �          0    34083    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    203   d�       �          0    34189    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    216   ��       �          0    34226    shop_category 
   TABLE DATA           1   COPY public.shop_category (id, name) FROM stdin;
    public          postgres    false    220   ��       �          0    34201    shop_product 
   TABLE DATA           ^   COPY public.shop_product (id, name, category_id, color, cost, description, image) FROM stdin;
    public          postgres    false    218   i�       �          0    34247    users_loyaltycard 
   TABLE DATA           ?   COPY public.users_loyaltycard (id, name, discount) FROM stdin;
    public          postgres    false    222   ��       �          0    34094    users_myuser 
   TABLE DATA           \   COPY public.users_myuser (id, password, last_login, email, is_active, is_admin) FROM stdin;
    public          postgres    false    205   O�       �          0    34256    users_profile 
   TABLE DATA           K   COPY public.users_profile (id, name, loyalty_card_id, user_id) FROM stdin;
    public          postgres    false    224   ��       �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    212            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    214            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);
          public          postgres    false    210            �           0    0    cart_cart_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.cart_cart_id_seq', 37, true);
          public          postgres    false    225            �           0    0    cart_cartitem_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.cart_cartitem_id_seq', 58, true);
          public          postgres    false    229            �           0    0    cart_order_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.cart_order_id_seq', 28, true);
          public          postgres    false    227            �           0    0    django_admin_log_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 113, true);
          public          postgres    false    208            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);
          public          postgres    false    206            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 31, true);
          public          postgres    false    202            �           0    0    shop_category_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.shop_category_id_seq', 6, true);
          public          postgres    false    219            �           0    0    shop_product_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.shop_product_id_seq', 12, true);
          public          postgres    false    217            �           0    0    users_loyaltycard_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.users_loyaltycard_id_seq', 6, true);
          public          postgres    false    221            �           0    0    users_myuser_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.users_myuser_id_seq', 9, true);
          public          postgres    false    204            �           0    0    users_profile_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.users_profile_id_seq', 6, true);
          public          postgres    false    223            �
           2606    34187    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    213                        2606    34173 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    215    215                       2606    34162 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    215            �
           2606    34152    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    213            �
           2606    34164 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    211    211            �
           2606    34144 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    211                       2606    34362    cart_cart cart_cart_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.cart_cart
    ADD CONSTRAINT cart_cart_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.cart_cart DROP CONSTRAINT cart_cart_pkey;
       public            postgres    false    226                       2606    34381     cart_cartitem cart_cartitem_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.cart_cartitem DROP CONSTRAINT cart_cartitem_pkey;
       public            postgres    false    230                       2606    34373    cart_order cart_order_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.cart_order
    ADD CONSTRAINT cart_order_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.cart_order DROP CONSTRAINT cart_order_pkey;
       public            postgres    false    228            �
           2606    34124 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    209            �
           2606    34112 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    207    207            �
           2606    34110 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    207            �
           2606    34091 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    203                       2606    34196 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    216                       2606    34231     shop_category shop_category_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.shop_category
    ADD CONSTRAINT shop_category_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.shop_category DROP CONSTRAINT shop_category_pkey;
       public            postgres    false    220            
           2606    34209    shop_product shop_product_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.shop_product
    ADD CONSTRAINT shop_product_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.shop_product DROP CONSTRAINT shop_product_pkey;
       public            postgres    false    218                       2606    34252 (   users_loyaltycard users_loyaltycard_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.users_loyaltycard
    ADD CONSTRAINT users_loyaltycard_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.users_loyaltycard DROP CONSTRAINT users_loyaltycard_pkey;
       public            postgres    false    222            �
           2606    34101 #   users_myuser users_myuser_email_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.users_myuser
    ADD CONSTRAINT users_myuser_email_key UNIQUE (email);
 M   ALTER TABLE ONLY public.users_myuser DROP CONSTRAINT users_myuser_email_key;
       public            postgres    false    205            �
           2606    34099    users_myuser users_myuser_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.users_myuser
    ADD CONSTRAINT users_myuser_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.users_myuser DROP CONSTRAINT users_myuser_pkey;
       public            postgres    false    205                       2606    34261     users_profile users_profile_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.users_profile DROP CONSTRAINT users_profile_pkey;
       public            postgres    false    224                       2606    34263 '   users_profile users_profile_user_id_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_user_id_key UNIQUE (user_id);
 Q   ALTER TABLE ONLY public.users_profile DROP CONSTRAINT users_profile_user_id_key;
       public            postgres    false    224            �
           1259    34188    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    213            �
           1259    34184 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    215                       1259    34185 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    215            �
           1259    34170 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    211                       1259    34387    cart_cart_user_id_9b4220b9    INDEX     S   CREATE INDEX cart_cart_user_id_9b4220b9 ON public.cart_cart USING btree (user_id);
 .   DROP INDEX public.cart_cart_user_id_9b4220b9;
       public            postgres    false    226                       1259    34404    cart_cartitem_cart_id_370ad265    INDEX     [   CREATE INDEX cart_cartitem_cart_id_370ad265 ON public.cart_cartitem USING btree (cart_id);
 2   DROP INDEX public.cart_cartitem_cart_id_370ad265;
       public            postgres    false    230                       1259    34405 !   cart_cartitem_product_id_b24e265a    INDEX     a   CREATE INDEX cart_cartitem_product_id_b24e265a ON public.cart_cartitem USING btree (product_id);
 5   DROP INDEX public.cart_cartitem_product_id_b24e265a;
       public            postgres    false    230                       1259    34393    cart_order_cart_id_3d97d381    INDEX     U   CREATE INDEX cart_order_cart_id_3d97d381 ON public.cart_order USING btree (cart_id);
 /   DROP INDEX public.cart_order_cart_id_3d97d381;
       public            postgres    false    228            �
           1259    34135 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    209            �
           1259    34136 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    209                       1259    34198 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    216                       1259    34197 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    216                       1259    34239 !   shop_product_category_id_14d7eea8    INDEX     a   CREATE INDEX shop_product_category_id_14d7eea8 ON public.shop_product USING btree (category_id);
 5   DROP INDEX public.shop_product_category_id_14d7eea8;
       public            postgres    false    218            �
           1259    34102     users_myuser_email_0bd4d201_like    INDEX     n   CREATE INDEX users_myuser_email_0bd4d201_like ON public.users_myuser USING btree (email varchar_pattern_ops);
 4   DROP INDEX public.users_myuser_email_0bd4d201_like;
       public            postgres    false    205                       1259    34274 &   users_profile_loyalty_card_id_76d4f464    INDEX     k   CREATE INDEX users_profile_loyalty_card_id_76d4f464 ON public.users_profile USING btree (loyalty_card_id);
 :   DROP INDEX public.users_profile_loyalty_card_id_76d4f464;
       public            postgres    false    224            "           2606    34179 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    2808    215    211            !           2606    34174 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    215    2813    213                        2606    34165 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    207    211    2799            &           2606    34382 7   cart_cart cart_cart_user_id_9b4220b9_fk_users_myuser_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.cart_cart
    ADD CONSTRAINT cart_cart_user_id_9b4220b9_fk_users_myuser_id FOREIGN KEY (user_id) REFERENCES public.users_myuser(id) DEFERRABLE INITIALLY DEFERRED;
 a   ALTER TABLE ONLY public.cart_cart DROP CONSTRAINT cart_cart_user_id_9b4220b9_fk_users_myuser_id;
       public          postgres    false    226    2795    205            (           2606    34394 <   cart_cartitem cart_cartitem_cart_id_370ad265_fk_cart_cart_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_cart_id_370ad265_fk_cart_cart_id FOREIGN KEY (cart_id) REFERENCES public.cart_cart(id) DEFERRABLE INITIALLY DEFERRED;
 f   ALTER TABLE ONLY public.cart_cartitem DROP CONSTRAINT cart_cartitem_cart_id_370ad265_fk_cart_cart_id;
       public          postgres    false    2837    226    230            )           2606    34399 B   cart_cartitem cart_cartitem_product_id_b24e265a_fk_shop_product_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_product_id_b24e265a_fk_shop_product_id FOREIGN KEY (product_id) REFERENCES public.shop_product(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.cart_cartitem DROP CONSTRAINT cart_cartitem_product_id_b24e265a_fk_shop_product_id;
       public          postgres    false    230    218    2826            '           2606    34388 6   cart_order cart_order_cart_id_3d97d381_fk_cart_cart_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.cart_order
    ADD CONSTRAINT cart_order_cart_id_3d97d381_fk_cart_cart_id FOREIGN KEY (cart_id) REFERENCES public.cart_cart(id) DEFERRABLE INITIALLY DEFERRED;
 `   ALTER TABLE ONLY public.cart_order DROP CONSTRAINT cart_order_cart_id_3d97d381_fk_cart_cart_id;
       public          postgres    false    228    226    2837                       2606    34125 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    209    2799    207                       2606    34130 E   django_admin_log django_admin_log_user_id_c564eba6_fk_users_myuser_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_myuser_id FOREIGN KEY (user_id) REFERENCES public.users_myuser(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_myuser_id;
       public          postgres    false    2795    209    205            #           2606    34240 B   shop_product shop_product_category_id_14d7eea8_fk_shop_category_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.shop_product
    ADD CONSTRAINT shop_product_category_id_14d7eea8_fk_shop_category_id FOREIGN KEY (category_id) REFERENCES public.shop_category(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.shop_product DROP CONSTRAINT shop_product_category_id_14d7eea8_fk_shop_category_id;
       public          postgres    false    2828    220    218            %           2606    34406 L   users_profile users_profile_loyalty_card_id_76d4f464_fk_users_loyaltycard_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_loyalty_card_id_76d4f464_fk_users_loyaltycard_id FOREIGN KEY (loyalty_card_id) REFERENCES public.users_loyaltycard(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.users_profile DROP CONSTRAINT users_profile_loyalty_card_id_76d4f464_fk_users_loyaltycard_id;
       public          postgres    false    222    2830    224            $           2606    34269 ?   users_profile users_profile_user_id_2112e78d_fk_users_myuser_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_user_id_2112e78d_fk_users_myuser_id FOREIGN KEY (user_id) REFERENCES public.users_myuser(id) DEFERRABLE INITIALLY DEFERRED;
 i   ALTER TABLE ONLY public.users_profile DROP CONSTRAINT users_profile_user_id_2112e78d_fk_users_myuser_id;
       public          postgres    false    2795    224    205            �      x������ � �      �      x������ � �      �     x�]�]��0F��UtW��<�6�4�h.S	Z��ilǱ���#q�gg~Mk5�s�ܫ����Q�~5�o����j ���G	�C�Z��.��@R���M۽�k���娡�����08H#	��c��x1te�����^��4�V��H;E����4T0)J�.�
M	6lz��eZ���ֵ�/�I��NZe���K@��ܶ5�_��7��Sz�n�:'���n'�%__��_�:�~{�q{���j
C���M(�1&v�@`�HنW���-�+[�](L���M(X���=(�WF�ܦ��۱(#�J�m�*�ɠ�~��/0��F\�}z��`�l�t<�)�ئ�D�|C��;�x>%���9Q4]�2����qA(�T�f<E���1r�Sƙ+!�^Tș�)#�D�!�(�m[�x���&�ѹ"��&���b��L�N}{�D�4�f�T۶?k0'\�>�
)DG-� �!V�`s���(l���"F�>3�C�{&@��_���X���      �   Y   x�%���0C�s<"IK�.����E��S%�I����5Wۯ��0���	�A;(�`,:\��
Ŭ���V��T6�pU��N����C�(:�      �   �   x��ɍ�0C�b1[K�����c�� 	#.�Nl�����*Z������s%��wt5�=p��>��|��r@���$Ʉg�0'9�9�Iv$ˬv�!�Hb�H�05���v��¤|��[.)L�V=a�^W���F��������ִ��w5���+)Ɓ���,�e��O�?�j-�      �   Y  x���Mn1���)zO���.WK܄A�p��D�\`���@�+�oDuG"3=Yı��L�Woʯ�J`��J  x�� 82���T�jπ��W�߄��]����]O�v埿�v;mڍ���OW��ɀ!`Ԁ\���<BM�D��a?�>+�,`�y��L���т��V��� �!	���"B�l�tЈK��00�s9"��uE�2rME��	j5"χ��:f�����SkD~�k��R�1��-�8P4��#H�,Y��J1��p�EK&��,F,���L���~��� Y���ZL�T�	r�]^n�Imo��c'�J�B"�g��S�뢂
�cs$YJ�[pO�)[�׉%��t>m���b�/ϧ�t�.��?�n���ݯ�����ӧ���C��n���f��S"*�0p���(2��Z����k��(xC1> �1y��dPU���k\�G�������N������H�˾�l ��r�Z���)�����P9@:��ԋ2`�XB`����^4��t�ȘHq߲��s�r������]�T�EJ�L��|��4I͕�������y�R�sh�h��<��]G||P�Ԝώ1�L1�4�Z      �   �  x���͎��ϣ�h�)�����Ϝ6�)����0�I�v��J�`�W�@Ű�9�V��"E��o�"�=?��x)�a���.�W�&&(P\��P��)���5���r����-o�ߙݩO�O`r�ӽ�|���M�O?��C�	\Ô�H�	8��ɍ��>�t��F��cr2_|�<ܿr<��eGW	�h*m-�SJzL��ڳ�Q��k�6/�W�˽�a�,3UP# �)��гnώnE�����p~��{c��wg�{��p����Z��*�t 5��V���_e �@~�PJ!.v�Ssټ���z��K�`��8EY[)M�����ŭ㓇��G^�V��ߎ�,�@a��F��M��s�س�=k^�8�r�T�R�#'Ϳ8f��_��9`jI	!R��;�<Ϥy���!=�E���i?�#T�`�MR(��t)PqL.ۯ�?��"�b@C��S"�����sټ�!��ѝ�Ҡ��{�	Z5ϛ�퓪�"��9�A��\m��h��$?���K���n�n�"�e���7!��4/B�7�a9�r)�K��-�ne��.��y����h(�4I�vFӭ��<�׼���y9�k�%H����L�G���aJ�b���)ԭ�Su��kw�P�4��U^cc�狻�˿p��xr|sy�k³T��2���X�F;���FF�Jaܰ����C`�ej���;��w󡭌nY�?��3q���?;9{� �C�t���W���qǫ�Qu����fu���Z86���p,����loX9^n�8��H�-6J�~ٮ	)H��gHt� �*�IL�T>��2�]������DJ�ݥ�-⦆cq

!!-�o�ߐ���H�_��X�����:��Xk�:�M��_�_e��4COP	���N�r�����9�M)���Ƥ�D������vOv��R��Iq1�b�RĘ�2%����C�����\!�
2@�z5���0������p2�3���J�Tg!�2�,¥
�8:T&�F	.M��c_��A.���C�*Q�KEHq��%�ԅ'A�Y��{�B�����ƭ��YA�V� ��
Yd�[�B��"+h�
,YlJEVи�"+(g��qEVP�
v6Њ��� "���� @q�Y��8��9�3N �O�"'t�	� w�"'t�	P]=�"'t�	 ��/rBg����(EN�ܲ;\�:���e���9)P(�Pd��Y��Ya2Vp#�pEV��lY�+��d�`�-b�&cPR�,��d�X㊬0+P��"+L�
�x� ER�����Ia2R���ZƉ�H	�S�v�"#����J�>l�'�8A�lʢĸ������
r�E��؝�-�M� �ey`c 	G�W�n�����V�(P�(�j�V� ;E��6�����ǫ�|Z��	�������Aw3#��?,��kh=��`�Z�)��9���x���ߝ-7���>�ٮ|<�KK�N��r2�Ӌ��u��j���;1���72����rW��J�)��������Σ\�ƿ�����!�������n�+�#`�U����V`��.���.���?��;g���5����;���ɜ������D	�a8��.k���䫚6 �;�\��.�I@�k��u2�������Tr����<�7�K8��:�u���wp@���B��Ư��
dv� I������ٝ LAnGl��pk��	�Nx���7��Fk:�׆�2�T��xXC(>]��G{�~�>
��5ϸv\�g��$A#@[hԔ�"�Ud?8~8;<}�Ӽ+�"�Ӂ����2��F�x���p(p5'd����H1y�m2�o	�+�����f�����
�E�',���6�k�X�]�@�(���D)���5j���W�60��
e/��������`��(`�\��csQ���U��{ּ�Γ�wN�/��yup{q��i�&�����}��}w��o�7�����]��'�      �   �   x�M�M!��p��N��ҍQ:c�b޾vf�v�/�<0�*I��?'�>��g�*O`�.PHR�5p��Ff�V����U���+TZ�;�����oN�Ig�fY�����F�ΊGs��0�B$4fDׂf����М6���7�"��K�      �   3  x����n�0���S�~U4��,+Y��I-��T�ۯ�PH�d�n��<��x�:�.� �񽟼m+^A�{l6j�
8��#�>����2�'�%0�������OH$I���b�pJ�Ƌ������=6�Ȍ�+���$3v?�ЛckOf��>��F�+J��N�j������s�$&�댒U���qLR�"+Ԣ ƶ��fp���=�Mg?M��S:����H�3*O�q���C
!��LAX0��?��0Lہ
ʵf����2Z;N�Y>Y;�����d�d��ԏ���KCJ�L��j]2A�@�\ɇm��N!�e\\�!�΍�=ݙ�A��1���f8�b�B��H�H�)��Z�	B�B�Q���sI栖�E4�!�����f藍@^��|����)ӫ�����u��G�#�:P�5ӊ��
�j|�����PVk�di'�EA�{'�&Hz�b�`�*��DF�Zw�A��eo�ͅ�Ah k*���X��[��F4j���r�*��;��@�U�$w��2b�k�7w"�S��ɝj�C�+���n��/��      �   A  x���ˎ�0���)f_MdlnR�!���Q�L�.!�� 	L�O�0U�ۮ�?����ׁڲ�R�޸�T�;�Gjh��||
���V.��WI^��;2U�"�<X�P��m��(x'��*�4�[Z<;l냶W�a���F��\qX�l����ʴ�D�K���VO���g�>��v��{��?s�HY�2Y��+�j#~���Ϲ��S؏�<�Ӕy��[��f�}U.�3X�|���H#s�<r��B���'@�^����gLll��u�00���Y%L-��6�&�UQ���_�I�ei�����ƺ��9��"�d���[�����Iҟچ�C��<���������lb�`�S��d'��dJr=r��;����Q��c�a7��zGL[��`���л���x<�ш/���� ���'On�yE�� ���`+��p��q�w1S{��(=U
��IG�?�Z2�Lz�9��_��Lqyߥ�V���_J.��H�L{,˿��3�6Esb�`X�h��I|A�ʳ�r��z�q;vy��ݗ��[gccnQB5c��5��f�zkpv      �   a   x����0C�)� ��4�@���At��*�썸��~v!8�����EK�F��=�V����Ik���:|���I�3h�-���Φ���]��?�)9       �   J  x�u��n1���S���3c��($)j��(MA��J�V�*ď`�i�4IK�+\���I�	��$����9�V��шni�C��wT�ĝR%A�x���X$J�t�T� �w�̗�#��
�����n��Ew���4��5I���Gi۵ם�݆�J��t+���TA֋	��q,��cw����*�h�l�toVX�JeY�F�43��i�����CwDwQD�!s�.���-~�����V��B`��伧�չ��R6.v��/��;�Ϋ�����f�g�3�,���x޼�s?�A0of]�M�*���F�RK��LX���1�I�E��V3�+]�SN |�-LN�o	gg���r��
F�4L}�53.�w�4d����Y�9����yX�r�1���ޞc�_����&80tT(���z�7����B���:<��!&\�-�Ii��T�FfJd�;�B/+���ZI������pƸ(b������1+���&|ߎ y#2�2�3�󛻔#)Q1�ɣ�1sC}M����������F���G('��C�i��]/�WNa;o�����7�-vb�NsӶ:�Jj�i����?�cMy      �   |   x�5�A�@�ӏ!���kx.G�ɛ��	Q����فx�I�:5�x��g��/?q�Te$㓃���?s^Q��x�r��Ew��7^�|�ɲS@6>�v�}���c��x��Go�,"���+ ?�yT�      �   o  x�m��n�@��c��pf��3�I�Xfi�n)��M6�GE�@��k�f���������$��U�)����vK�����h��̕�B9���p��Tz�z�G�i�rQ/�7
}`}�W�,�:GPe���(/��Z��L���{fq�WǦ��pc��롃d��C�i��<���'[.k�ءS��"����8��-��&���3_��h���o�6�%i�!.g��Y(��xv��O�W��㸜E��7��'nw�Oi/Ns(���ɢ���2\>gPЉiB�3�UZ�/]������E��j&X��������>iES�۝�:��+I��}v��#j�B��MJ����A���R몪�zg��      �   O   x�3估�{.6_lP�0�� g�}6q�pr�p��qr�sq^�|a+PfÅ-@;9�8M��@�&��\1z\\\ �R�     